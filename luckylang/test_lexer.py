import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from luckylang.lexer import tokenize

try:
    tokens = tokenize('fn test() { print "hello" }')
    for tok in tokens:
        print(f'{tok.kind}: {tok.value} line={tok.line} col={tok.col}')
except Exception as e:
    print(f'Error: {e}')

try:
    tokens = tokenize('x = 5')
    for tok in tokens:
        print(f'{tok.kind}: {tok.value} line={tok.line} col={tok.col}')
except Exception as e:
    print(f'Error: {e}')

try:
    tokens = tokenize('if x > 10 { print "big" }')
    for tok in tokens:
        print(f'{tok.kind}: {tok.value} line={tok.line} col={tok.col}')
except Exception as e:
    print(f'Error: {e}')

try:
    tokens = tokenize('# comment\n// another comment\n')
    for tok in tokens:
        print(f'{tok.kind}: {tok.value} line={tok.line} col={tok.col}')
except Exception as e:
    print(f'Error: {e}')

print("\n✅ Lexer tests completed!")