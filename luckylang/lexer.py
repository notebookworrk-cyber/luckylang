import re

TOKEN_SPEC = [
    ("NUMBER",   r"\d+(\.\d+)?"),
    ("STRING",   r'"[^"]*"'),
    ("IDENT",    r"[a-zA-Z_][a-zA-Z0-9_]*"),
    ("FN",       r"fn"),
    ("RETURN",   r"return"),
    ("ASSIGN",   r"="),
    ("PLUS",     r"\+"),
    ("MINUS",    r"-"),
    ("MUL",      r"\*"),
    ("DIV",      r"/"),
    ("GT",       r">"),
    ("LT",       r"<"),
    ("EQ",       r"=="),
    ("NE",       r"!="),
    ("GTE",      r">="),
    ("LTE",      r"<="),
    ("AND",      r"and"),
    ("OR",       r"or"),
    ("NOT",      r"not"),
    ("COMMA",    r","),
    ("COLON",    r":"),
    ("LPAREN",   r"\("),
    ("RPAREN",   r"\)"),
    ("LBRACE",   r"\{"),
    ("RBRACE",   r"\}"),
    ("LBRACKET", r"\["),
    ("RBRACKET", r"\]"),
    ("NEWLINE",  r"\n"),
    ("SKIP",     r"[ \t]+"),
    ("COMMENT",  r"(//|#)[^\n]*"),
    ("MISMATCH", r"."),
]

TOKEN_RE = re.compile("|".join(f"(?P<{name}>{pattern})" for name, pattern in TOKEN_SPEC))


class Token:
    def __init__(self, kind, value, line, col):
        self.kind = kind
        self.value = value
        self.line = line
        self.col = col

    def __repr__(self):
        return f"Token({self.kind}, {self.value!r}, line={self.line}, col={self.col})"


def tokenize(source):
    tokens = []
    line = 1
    col = 1
    for m in TOKEN_RE.finditer(source):
        kind = m.lastgroup
        value = m.group()
        if kind == "NEWLINE":
            tokens.append(Token("NEWLINE", "\n", line, col))
            line += 1
            col = 1
        elif kind == "SKIP" or kind == "COMMENT":
            col += len(value)
        elif kind == "MISMATCH":
            raise SyntaxError(f"Unexpected character {value!r} at line {line}, col {col}")
        else:
            tokens.append(Token(kind, value, line, col))
            col += len(value)
    tokens.append(Token("EOF", "", line, col))
    return tokens