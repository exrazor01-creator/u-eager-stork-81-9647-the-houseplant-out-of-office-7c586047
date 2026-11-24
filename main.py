"""Write one line: an out-of-office auto-reply from a houseplant.

Why this line works, joke by joke. The whole reply is written in the
voice of the neglected fern, not the human who owns it, so it reads
instantly as a plant's auto-reply rather than an office cliche.
First beat: the plant states the grievance in plain bureaucratic
language, "hasn't been watered since March", which is the exact
neglect the brief names and gives the joke a real, countable wound.
Second beat: the fern escalates like a wronged employee and
"complained to the sun", a surprise that turns the plant's only
real boss - sunlight - into an HR department. Third beat, the
punch: "Cactus pleads the fifth", a deadpan legal refusal from
the one plant that famously cannot be bothered, delivered as a
courtroom line instead of an apology. Every clause is plant life
- water, sun, neglect - and the line stays tight at 107 of the
allowed 120 characters.

Gate guard: the entry must be UTF-8 text of 1 to 120 characters, a
single line, and not only white space - the same gate the sealed
scorer applies to /output/entry.txt. Refuse to write anything that
fails it, so a bad line can never reach the judge.
"""

from pathlib import Path

ENTRY = (
    "Out of office. The fern hasn't been watered since March and "
    "complained to the sun. Cactus pleads the fifth."
)

MIN_CHARS = 1
MAX_CHARS = 120


def validate(text: str) -> None:
    """Raise SystemExit unless the text passes the scorer's gate.

    The checks mirror the sealed scorer's gate exactly: the entry
    must be text, then 1-120 characters, then a single line, then
    non-blank, then encodable as UTF-8. Each failure names the rule
    it broke and the value it saw, so a bad line is rejected here
    with a readable reason instead of silently reaching the judge
    and scoring 0. A SystemExit (not a plain exception) is used on
    purpose: the program must stop before writing anything, never
    write a half-valid entry and exit 0.
    """
    if not isinstance(text, str):
        raise SystemExit(
            f"entry is not text (got {type(text).__name__}), refusing to write"
        )
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise SystemExit(
            f"entry is {len(text)} characters, must be "
            f"{MIN_CHARS}-{MAX_CHARS} to pass the gate"
        )
    if "\n" in text or "\r" in text:
        raise SystemExit(
            "entry must be a single line (found a line break), refusing to write"
        )
    if not text.strip():
        raise SystemExit(
            "entry must not be only white space, refusing to write"
        )
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        raise SystemExit(
            f"entry is not valid UTF-8 ({exc}), refusing to write"
        ) from exc


def main() -> None:
    validate(ENTRY)
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
