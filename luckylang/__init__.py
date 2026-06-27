from .lexer import tokenize
from .parser import parse
from .interpreter import interpret

def run(source: str):
    tokens = tokenize(source)
    ast = parse(tokens)
    interpret(ast)
