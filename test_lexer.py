import sys
sys.path.insert(0, 'luckylang')
from luckylang.lexer import tokenize

print('Lexer tests:')
tokens = tokenize('fn test() { print "hello" }')
for tok in tokens:
    print(f'  {tok.kind}: {tok.value} line={tok.line} col={tok.col}')

print()
tokens = tokenize('x = 5')
for tok in tokens:
    print(f'  {tok.kind}: {tok.value} line={tok.line} col={tok.col}')

print()
tokens = tokenize('if x > 10 { print "big" }')
for tok in tokens:
    print(f'  {tok.kind}: {tok.value} line={tok.line} col={tok.col}')

print()
tokens = tokenize('# comment\n// another comment\n')
for tok in tokens:
    print(f'  {tok.kind}: {tok.value} line={tok.line} col={tok.col}')

print("\n✅ Lexer tests completed!")