import re

TOKEN_SPEC = [
    ("NUMBER",   r"\d+(\.\d+)?"),
    ("STRING",   r'"[^"]*"'),
    ("IDENT",    r"[a-zA-Z_][a-zA-Z0-9_]*"),
    ("ASSIGN",   r"="),
    ("PLUS",     r"\+"),
    ("MINUS",    r"-"),
    ("MUL",      r"\*"),
    ("DIV",      r"/"),
    ("GT",       r">"),
    ("LT",       r"<"),
    ("EQ",       r"=="),
    ("LPAREN",   r"\("),
    ("RPAREN",   r"\)"),
    ("LBRACE",   r"\{"),
    ("RBRACE",   r"\}"),
    ("NEWLINE",  r"\n"),
    ("SKIP",     r"[ \t]+"),
    ("COMMENT",  r"//[^\n]*"),
    ("MISMATCH", r"."),
]

TOKEN_RE = re.compile("|".join(f"(?P<{name}>{pattern})" for name, pattern in TOKEN_SPEC))


class Token:
    def __init__(self, kind, value, line):
        self.kind = kind
        self.value = value
        self.line = line

    def __repr__(self):
        return f"Token({self.kind}, {self.value!r}, line={self.line})"


def tokenize(source):
    tokens = []
    line = 1
    for m in TOKEN_RE.finditer(source):
        kind = m.lastgroup
        value = m.group()
        if kind == "NEWLINE":
            tokens.append(Token("NEWLINE", "\n", line))
            line += 1
        elif kind == "SKIP" or kind == "COMMENT":
            continue
        elif kind == "MISMATCH":
            raise SyntaxError(f"Unexpected character {value!r} at line {line}")
        else:
            tokens.append(Token(kind, value, line))
    tokens.append(Token("EOF", "", line))
    return tokens
