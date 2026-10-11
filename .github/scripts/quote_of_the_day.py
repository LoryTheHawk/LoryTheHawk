"""Replace the quote block in the README with the quote for today's date."""

import datetime
import re
import sys

QUOTES = [
    ("Price is what you pay. Value is what you get.", "Warren Buffett"),
    ("Risk comes from not knowing what you're doing.", "Warren Buffett"),
    ("Be fearful when others are greedy and greedy when others are fearful.", "Warren Buffett"),
    ("The stock market is a device for transferring money from the impatient to the patient.", "Warren Buffett"),
    ("In the short run, the market is a voting machine but in the long run, it is a weighing machine.", "Benjamin Graham"),
    ("Know what you own, and know why you own it.", "Peter Lynch"),
    ("The four most dangerous words in investing are: 'this time it's different.'", "Sir John Templeton"),
    ("Diversification is the only free lunch in finance.", "Harry Markowitz"),
    ("Be prepared.", "Robert Baden-Powell"),
    ("Try and leave this world a little better than you found it.", "Robert Baden-Powell"),
]

START = "<!--QUOTE:START-->"
END = "<!--QUOTE:END-->"


def main(path):
    text, author = QUOTES[datetime.date.today().toordinal() % len(QUOTES)]
    block = f'{START}\n> *"{text}"*\n> — **{author}**\n{END}'

    with open(path, encoding="utf-8") as f:
        readme = f.read()

    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.DOTALL)
    if not pattern.search(readme):
        sys.exit(f"Quote markers not found in {path}")

    with open(path, "w", encoding="utf-8") as f:
        f.write(pattern.sub(lambda _: block, readme))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "README.md")
