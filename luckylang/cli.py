import argparse
import sys
from . import run
from .repl import main as repl_main
from .version import __version__


def run_file(filepath):
    try:
        with open(filepath, 'r') as f:
            source = f.read()
        run(source)
        print(f"✓ Executed {filepath}")
    except FileNotFoundError:
        print(f"✗ File not found: {filepath}")
        sys.exit(1)
    except Exception as e:
        print(f"✗ Error in {filepath}: {e}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        prog="lukylang",
        description="Lukylang - A simple programming language for learning and scripting",
        epilog="Examples:\n  lukylang examples/hello.lucky\n  lukylang --repl\n  lukylang --version"
    )

    parser.add_argument(
        'file',
        nargs='?',
        help="Lukylang source file to execute"
    )

    parser.add_argument(
        '-r', '--repl',
        action='store_true',
        help="Start interactive REPL session"
    )

    parser.add_argument(
        '-v', '--version',
        action='store_true',
        help="Show version information"
    )

    parser.add_argument(
        '--examples',
        action='store_true',
        help="Show example programs and exit"
    )

    args = parser.parse_args()

    if args.version:
        print(f"Lukylang {__version__}")
        print("A simple, educational programming language")
        sys.exit(0)

    if args.examples:
        from .repl import LuckylangREPL
        repl = LuckylangREPL()
        repl.examples()
        sys.exit(0)

    if args.repl:
        repl_main()

    if args.file:
        run_file(args.file)

    if not any([args.file, args.repl, args.examples, args.version]):
        parser.print_help()
        print("\nTry: lukylang --help\n  or: lukylang --examples\n  or: lukylang --repl")
        sys.exit(1)