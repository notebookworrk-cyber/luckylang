from luckylang.interpreter import Interpreter
import sys

try:
    interp = Interpreter()
    print("Interpreter initialized successfully")
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)