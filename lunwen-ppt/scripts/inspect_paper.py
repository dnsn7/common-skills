#!/usr/bin/env python
import argparse
import json
import re
import shutil
import subprocess
from pathlib import Path
from pypdf import PdfReader


def main():
    ap = argparse.ArgumentParser(description="Extract reusable paper evidence and optional page renders.")
    ap.add_argument("pdf")
    ap.add_argument("--out", required=True)
    ap.add_argument("--render-dir")
    ap.add_argument("--dpi", type=int, default=110)
    args = ap.parse_args()

    pdf = Path(args.pdf).resolve()
    out = Path(args.out).resolve()
    out.parent.mkdir(parents=True, exist_ok=True)
    reader = PdfReader(str(pdf))
    pages = []
    for index, page in enumerate(reader.pages, 1):
        text = page.extract_text() or ""
        captions = re.findall(r"(?ims)(?:Fig\.|Figure|Table)\s*\d+[^\n]*(?:\n(?!\n).*){0,8}", text)
        pages.append({"page": index, "text": text, "captions": captions})
    meta = {str(k).lstrip("/"): str(v) for k, v in (reader.metadata or {}).items()}
    payload = {
        "source_pdf": str(pdf),
        "page_count": len(reader.pages),
        "metadata": meta,
        "doi": meta.get("doi") or meta.get("Subject", ""),
        "pages": pages,
    }
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    if args.render_dir:
        render_dir = Path(args.render_dir).resolve()
        render_dir.mkdir(parents=True, exist_ok=True)
        pdftoppm = shutil.which("pdftoppm")
        if not pdftoppm:
            raise SystemExit("paper.json created; pdftoppm not found, so pages were not rendered")
        subprocess.run(
            [pdftoppm, "-png", "-r", str(args.dpi), str(pdf), str(render_dir / "page")],
            check=True,
        )
    print(out)


if __name__ == "__main__":
    main()
