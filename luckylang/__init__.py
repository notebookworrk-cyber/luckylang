from .lexer import tokenize
from .parser import parse
from .interpreter import interpret
from .errors import LexError, ParseError, RuntimeError, InterpreterError

def run(source: str):
    tokens = tokenize(source)
    ast = parse(tokens)
    interpret(ast)
