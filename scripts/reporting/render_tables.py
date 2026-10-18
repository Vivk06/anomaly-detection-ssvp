"""Render the curated CSVs as Markdown tables and update README results."""

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RESULTS = ROOT / "results"


def read_rows(path):
    with path.open(newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def table(headers, rows):
    def cell(value):
        return str(value or "").replace("|", "\\|").replace("\n", " ")
    lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join("---" for _ in headers) + " |"]
    lines.extend("| " + " | ".join(cell(value) for value in row) + " |" for row in rows)
    return "\n".join(lines) + "\n"


def render():
    metrics = read_rows(RESULTS / "metrics.csv")
    captions = read_rows(RESULTS / "captions.csv")
    tables = RESULTS / "tables"
    tables.mkdir(parents=True, exist_ok=True)

    selected = [row for row in metrics if
        row["run_id"] == "run21_resplit_15es" or
        (row["run_id"] in {"anomalyclip_d2_cable", "winclip_summary_cable"} and row["eval"] == "clean")]
    summary = "## Selected results\n\n" + table(
        ["Model", "Title", "Eval", "Image AUROC", "Pixel AUROC", "Pixel PRO"],
        [[row[key] for key in ("model", "title", "eval", "image_auroc", "pixel_auroc", "pixel_pro")] for row in selected],
    )
    (tables / "summary.md").write_text(summary, encoding="utf-8")
    metric_table = "# All reported metrics\n\n" + table(
        ["Run ID", "Title", "Model", "Status", "Eval", "Categories", "Resolution", "Noise", "I-AUROC", "I-F1", "I-AP", "P-AUROC", "P-PRO", "P-AP"],
        [[row[key] for key in ("run_id", "title", "model", "status", "eval", "categories", "resolution", "noise_protocol", "image_auroc", "image_f1_max", "image_ap", "pixel_auroc", "pixel_pro", "pixel_ap")] for row in metrics],
    )
    (tables / "metrics.md").write_text(metric_table, encoding="utf-8")
    caption_table = "# Caption evaluations\n\n" + table(
        ["Eval ID", "Title", "Variant", "Split", "Images", "BERTScore F1", "Notes"],
        [[row[key] for key in ("eval_id", "title", "variant", "split", "n_images", "bertscore_f1", "notes")] for row in captions],
    )
    (tables / "captions.md").write_text(caption_table, encoding="utf-8")

    readme = ROOT / "README.md"
    text = readme.read_text(encoding="utf-8")
    start = "<!-- results:start -->"
    end = "<!-- results:end -->"
    assert text.count(start) == text.count(end) == 1
    left, rest = text.split(start, 1)
    _, right = rest.split(end, 1)
    readme.write_text(left + start + "\n" + summary + end + right, encoding="utf-8")


if __name__ == "__main__":
    render()
