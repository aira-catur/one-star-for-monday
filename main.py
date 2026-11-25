import os

TEXT = "One star. Seated at 6 a.m. sharp, served cold Sunday leftovers, and the waiter, Weekend, never came back to my table."


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
