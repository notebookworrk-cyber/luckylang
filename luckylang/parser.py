class AST:
    pass

class Number(AST):
    def __init__(self, value, line=0, col=0):
        self.value = value
        self.line = line
        self.col = col

class String(AST):
    def __init__(self, value, line=0, col=0):
        self.value = value
        self.line = line
        self.col = col

class Ident(AST):
    def __init__(self, name, line=0, col=0):
        self.name = name
        self.line = line
        self.col = col

class Assign(AST):
    def __init__(self, name, expr, line=0, col=0):
        self.name = name
        self.expr = expr
        self.line = line
        self.col = col

class BinOp(AST):
    def __init__(self, op, left, right, line=0, col=0):
        self.op = op
        self.left = left
        self.right = right
        self.line = line
        self.col = col

class Print(AST):
    def __init__(self, expr, line=0, col=0):
        self.expr = expr
        self.line = line
        self.col = col

class If(AST):
    def __init__(self, cond, body, line=0, col=0):
        self.cond = cond
        self.body = body
        self.line = line
        self.col = col

class Loop(AST):
    def __init__(self, count, body, line=0, col=0):
        self.count = count
        self.body = body
        self.line = line
        self.col = col

class Block(AST):
    def __init__(self, statements, line=0, col=0):
        self.statements = statements
        self.line = line
        self.col = col

class Function(AST):
    def __init__(self, name, params, body, line=0, col=0):
        self.name = name
        self.params = params
        self.body = body
        self.line = line
        self.col = col

class Call(AST):
    def __init__(self, callee, args, line=0, col=0):
        self.callee = callee
        self.args = args
        self.line = line
        self.col = col

class Return(AST):
    def __init__(self, expr, line=0, col=0):
        self.expr = expr
        self.line = line
        self.col = col

class List(AST):
    def __init__(self, elements, line=0, col=0):
        self.elements = elements
        self.line = line
        self.col = col

class Dict(AST):
    def __init__(self, pairs, line=0, col=0):
        self.pairs = pairs
        self.line = line
        self.col = col

class Index(AST):
    def __init__(self, obj, index, line=0, col=0):
        self.obj = obj
        self.index = index
        self.line = line
        self.col = col

class MethodCall(AST):
    def __init__(self, obj, method, args, line=0, col=0):
        self.obj = obj
        self.method = method
        self.args = args
        self.line = line
        self.col = col


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def peek(self):
        return self.tokens[self.pos]

    def consume(self, kind=None):
        tok = self.peek()
        if kind and tok.kind != kind:
            raise SyntaxError(f"Expected {kind}, got {tok.kind} at line {tok.line}, col {tok.col}")
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
        if tok.kind == "FN":
            return self.parse_fn_def()
        if tok.kind == "RETURN":
            return self.parse_return()
        if tok.kind == "IDENT" and tok.value == "print":
            return self.parse_print()
        if tok.kind == "IDENT" and tok.value == "if":
            return self.parse_if()
        if tok.kind == "IDENT" and tok.value == "loop":
            return self.parse_loop()
        if tok.kind == "IDENT" and tok.value == "import":
            return self.parse_import()
        return self.parse_assign_or_expr()

    def parse_fn_def(self):
        tok = self.consume("FN")
        name_tok = self.consume("IDENT")
        self.consume("LPAREN")
        params = []
        if self.peek().kind != "RPAREN":
            params.append(self.consume("IDENT").value)
            while self.peek().kind == "COMMA":
                self.consume("COMMA")
                params.append(self.consume("IDENT").value)
        self.consume("RPAREN")
        if self.peek().kind == "NEWLINE":
            self.consume("NEWLINE")
        self.consume("LBRACE")
        body = self.parse_block()
        self.consume("RBRACE")
        return Function(name_tok.value, params, body, tok.line, tok.col)

    def parse_return(self):
        tok = self.consume("RETURN")
        expr = self.parse_expr()
        self.consume("NEWLINE")
        return Return(expr, tok.line, tok.col)

    def parse_print(self):
        tok = self.consume("IDENT")
        expr = self.parse_expr()
        self.consume("NEWLINE")
        return Print(expr, tok.line, tok.col)

    def parse_if(self):
        tok = self.consume("IDENT")
        cond = self.parse_expr()
        if self.peek().kind == "NEWLINE":
            self.consume("NEWLINE")
        self.consume("LBRACE")
        body = self.parse_block()
        self.consume("RBRACE")
        return If(cond, body, tok.line, tok.col)

    def parse_loop(self):
        tok = self.consume("IDENT")
        count = self.parse_expr()
        if self.peek().kind == "NEWLINE":
            self.consume("NEWLINE")
        self.consume("LBRACE")
        body = self.parse_block()
        self.consume("RBRACE")
        return Loop(count, body, tok.line, tok.col)

    def parse_import(self):
        tok = self.consume("IDENT")
        path_tok = self.consume("STRING")
        path = path_tok.value[1:-1]
        alias = None
        if self.peek().kind == "IDENT" and self.peek().value == "as":
            self.consume("IDENT")
            alias = self.consume("IDENT").value
        self.consume("NEWLINE")
        return Import(path, alias, tok.line, tok.col)

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
            return Assign(tok.value, expr, tok.line, tok.col)
        expr = self.parse_expr()
        self.consume("NEWLINE")
        return expr

    def parse_expr(self):
        return self.parse_logical_or()

    def parse_logical_or(self):
        left = self.parse_logical_and()
        while self.peek().kind == "OR":
            op = self.consume().kind
            right = self.parse_logical_and()
            left = BinOp(op, left, right, left.line, left.col)
        return left

    def parse_logical_and(self):
        left = self.parse_comparison()
        while self.peek().kind == "AND":
            op = self.consume().kind
            right = self.parse_comparison()
            left = BinOp(op, left, right, left.line, left.col)
        return left

    def parse_comparison(self):
        left = self.parse_term()
        while self.peek().kind in ("EQ", "NE", "GT", "LT", "GTE", "LTE"):
            op = self.consume().kind
            right = self.parse_term()
            left = BinOp(op, left, right, left.line, left.col)
        return left

    def parse_term(self):
        left = self.parse_factor()
        while self.peek().kind in ("PLUS", "MINUS"):
            op = self.consume().kind
            right = self.parse_factor()
            left = BinOp(op, left, right, left.line, left.col)
        return left

    def parse_factor(self):
        left = self.parse_unary()
        while self.peek().kind in ("MUL", "DIV"):
            op = self.consume().kind
            right = self.parse_unary()
            left = BinOp(op, left, right, left.line, left.col)
        return left

    def parse_unary(self):
        tok = self.peek()
        if tok.kind in ("NOT", "MINUS"):
            op = self.consume().kind
            expr = self.parse_unary()
            return BinOp(op, Number(0), expr, tok.line, tok.col)
        return self.parse_call()

    def parse_call(self):
        expr = self.parse_primary()
        while True:
            tok = self.peek()
            if tok.kind == "LPAREN":
                self.consume("LPAREN")
                args = []
                if self.peek().kind != "RPAREN":
                    args.append(self.parse_expr())
                    while self.peek().kind == "COMMA":
                        self.consume("COMMA")
                        args.append(self.parse_expr())
                self.consume("RPAREN")
                expr = Call(expr, args, expr.line, expr.col)
            elif tok.kind == "LBRACKET":
                self.consume("LBRACKET")
                index = self.parse_expr()
                self.consume("RBRACKET")
                expr = Index(expr, index, expr.line, expr.col)
            elif tok.kind == "IDENT":
                # Could be method call - but we'd need to check for LPAREN next
                # For simplicity, handle method calls via dot notation later
                break
            else:
                break
        return expr

    def parse_primary(self):
        tok = self.peek()
        if tok.kind == "NUMBER":
            self.consume("NUMBER")
            return Number(float(tok.value) if "." in tok.value else int(tok.value), tok.line, tok.col)
        if tok.kind == "STRING":
            self.consume("STRING")
            return String(tok.value[1:-1], tok.line, tok.col)
        if tok.kind == "IDENT":
            self.consume("IDENT")
            return Ident(tok.value, tok.line, tok.col)
        if tok.kind == "LPAREN":
            self.consume("LPAREN")
            expr = self.parse_expr()
            self.consume("RPAREN")
            return expr
        if tok.kind == "LBRACKET":
            return self.parse_list()
        if tok.kind == "LBRACE":
            return self.parse_dict()
        raise SyntaxError(f"Unexpected token {tok.kind} at line {tok.line}, col {tok.col}")

    def parse_list(self):
        tok = self.consume("LBRACKET")
        elements = []
        if self.peek().kind != "RBRACKET":
            elements.append(self.parse_expr())
            while self.peek().kind == "COMMA":
                self.consume("COMMA")
                elements.append(self.parse_expr())
        self.consume("RBRACKET")
        return List(elements, tok.line, tok.col)

    def parse_dict(self):
        tok = self.consume("LBRACE")
        pairs = []
        if self.peek().kind != "RBRACE":
            key = self.parse_expr()
            self.consume("COLON")
            value = self.parse_expr()
            pairs.append((key, value))
            while self.peek().kind == "COMMA":
                self.consume("COMMA")
                key = self.parse_expr()
                self.consume("COLON")
                value = self.parse_expr()
                pairs.append((key, value))
        self.consume("RBRACE")
        return Dict(pairs, tok.line, tok.col)


class Import(AST):
    def __init__(self, path, alias, line=0, col=0):
        self.path = path
        self.alias = alias
        self.line = line
        self.col = col


def parse(tokens):
    return Parser(tokens).parse()