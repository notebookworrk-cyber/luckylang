class AST:
    pass

class Number(AST):
    def __init__(self, value):
        self.value = value

class String(AST):
    def __init__(self, value):
        self.value = value

class Ident(AST):
    def __init__(self, name):
        self.name = name

class Assign(AST):
    def __init__(self, name, expr):
        self.name = name
        self.expr = expr

class BinOp(AST):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

class Print(AST):
    def __init__(self, expr):
        self.expr = expr

class If(AST):
    def __init__(self, cond, body):
        self.cond = cond
        self.body = body

class Loop(AST):
    def __init__(self, count, body):
        self.count = count
        self.body = body

class Block(AST):
    def __init__(self, statements):
        self.statements = statements


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        return self.tokens[self.pos]

    def consume(self, kind=None):
        tok = self.peek()
        if kind and tok.kind != kind:
            raise SyntaxError(f"Expected {kind}, got {tok.kind} at line {tok.line}")
        self.pos += 1
        return tok

    def parse(self):
        statements = []
        while self.peek().kind != "EOF":
            stmt = self.parse_stmt()
            if stmt:
                statements.append(stmt)
        return Block(statements)

    def parse_stmt(self):
        tok = self.peek()
        if tok.kind == "NEWLINE":
            self.consume("NEWLINE")
            return None
        if tok.kind == "EOF":
            return None
        if tok.kind == "IDENT" and tok.value == "print":
            return self.parse_print()
        if tok.kind == "IDENT" and tok.value == "if":
            return self.parse_if()
        if tok.kind == "IDENT" and tok.value == "loop":
            return self.parse_loop()
        return self.parse_assign_or_expr()

    def parse_print(self):
        self.consume("IDENT")
        expr = self.parse_expr()
        self.consume("NEWLINE")
        return Print(expr)

    def parse_if(self):
        self.consume("IDENT")
        cond = self.parse_expr()
        if self.peek().kind == "NEWLINE":
            self.consume("NEWLINE")
        self.consume("LBRACE")
        body = self.parse_block()
        self.consume("RBRACE")
        return If(cond, body)

    def parse_loop(self):
        self.consume("IDENT")
        count = self.parse_expr()
        if self.peek().kind == "NEWLINE":
            self.consume("NEWLINE")
        self.consume("LBRACE")
        body = self.parse_block()
        self.consume("RBRACE")
        return Loop(count, body)

    def parse_block(self):
        statements = []
        while self.peek().kind not in ("RBRACE", "EOF"):
            stmt = self.parse_stmt()
            if stmt:
                statements.append(stmt)
        return Block(statements)

    def parse_assign_or_expr(self):
        tok = self.peek()
        if tok.kind == "IDENT" and self.pos + 1 < len(self.tokens) and self.tokens[self.pos + 1].kind == "ASSIGN":
            self.consume("IDENT")
            self.consume("ASSIGN")
            expr = self.parse_expr()
            self.consume("NEWLINE")
            return Assign(tok.value, expr)
        expr = self.parse_expr()
        self.consume("NEWLINE")
        return expr

    def parse_expr(self):
        left = self.parse_primary()
        while self.peek().kind in ("PLUS", "MINUS", "MUL", "DIV", "GT", "LT", "EQ"):
            op = self.consume().kind
            right = self.parse_primary()
            left = BinOp(op, left, right)
        return left

    def parse_primary(self):
        tok = self.peek()
        if tok.kind == "NUMBER":
            self.consume("NUMBER")
            return Number(float(tok.value) if "." in tok.value else int(tok.value))
        if tok.kind == "STRING":
            self.consume("STRING")
            return String(tok.value[1:-1])
        if tok.kind == "IDENT":
            self.consume("IDENT")
            return Ident(tok.value)
        if tok.kind == "LPAREN":
            self.consume("LPAREN")
            expr = self.parse_expr()
            self.consume("RPAREN")
            return expr
        raise SyntaxError(f"Unexpected token {tok.kind} at line {tok.line}")


def parse(tokens):
    return Parser(tokens).parse()
