import sys
from . import run


def main():
    if len(sys.argv) < 2:
        print("Usage: luckylang <file.lucky>")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        run(f.read())
