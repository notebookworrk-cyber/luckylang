class LexError(Exception):
    def __init__(self, message, line=0, col=0):
        super().__init__(f"Lex Error at line {line}, col {col}: {message}")
        self.line = line
        self.col = col

class ParseError(Exception):
    def __init__(self, message, line=0, col=0):
        super().__init__(f"Parse Error at line {line}, col {col}: {message}")
        self.line = line
        self.col = col


class RuntimeError(Exception):
    def __init__(self, message, line=0, col=0):
        super().__init__(f"Runtime Error at line {line}, col {col}: {message}")
        self.line = line
        self.col = col


class InterpreterError(RuntimeError):
    def __init__(self, message, line=0, col=0):
        super().__init__(message, line, col)