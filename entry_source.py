import os
from pathlib import Path

weekend_waiter_verdict_qm47 = (
    "One star. Seated at 6 a.m. sharp, served cold Sunday leftovers, and the waiter, Weekend, never came back to my table."
)


def main():
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(weekend_waiter_verdict_qm47, encoding="utf-8")


if __name__ == "__main__":
    main()
