import re
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
DOC_ROOTS = {"docs", "results", "data", "scripts", "report", "third_party"}
RUNTIME = ("outputs/", "data/mvtec/")


def docs():
    yield ROOT / "README.md"
    yield ROOT / "THIRD_PARTY.md"
    for folder in DOC_ROOTS:
        yield from (ROOT / folder).rglob("*.md") if (ROOT / folder).exists() else ()


def test_document_links_and_repo_paths_exist():
    failures = []
    for doc in docs():
        text = doc.read_text(encoding="utf-8")
        if "file:///" in text:
            failures.append(f"{doc}: file URI")
        for raw in re.findall(r"\]\(([^)]+)\)", text):
            path_part = raw.split("#", 1)[0].strip()
            if not path_part:
                continue
            destination = unquote(path_part.split()[0])
            if not destination or re.match(r"^[a-z]+://", destination) or destination.startswith("<"):
                continue
            if not (doc.parent / destination).exists():
                failures.append(f"{doc}: broken link {destination}")
        for token in re.findall(r"`([^`]+)`", text):
            if "<" in token or "*" in token or token.startswith(".") or token.startswith(RUNTIME):
                continue
            if not ("/" in token or token.endswith((".md", ".py", ".csv", ".json", ".yaml", ".pdf"))):
                continue
            if token.startswith(("http:", "https:", "arXiv")) or " " in token or token.startswith("--"):
                continue
            candidate = token.rstrip("/")
            if not ((ROOT / candidate).exists() or (doc.parent / candidate).exists()):
                failures.append(f"{doc}: missing path {token}")
    assert not failures, "\n".join(failures)
