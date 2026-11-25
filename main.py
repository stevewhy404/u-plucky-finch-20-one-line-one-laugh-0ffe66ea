"""One Line, One Laugh — writes a single funny line to /output/entry.txt."""

import os


LINE = "My calendar finally approved my day off, then booked a meeting over it called 'Rest (optional, bring laptop)'."


def verify(text: str) -> None:
    if not isinstance(text, str) or not text.strip():
        raise SystemExit("entry must not be blank")
    if len(text) > 200:
        raise SystemExit(f"entry is {len(text)} characters, over the 200 limit")
    if "\n" in text.strip():
        raise SystemExit("entry must be a single line")


def main() -> None:
    verify(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
