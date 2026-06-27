from .parser import Number, String, Ident, Assign, BinOp, Print, If, Loop, Block


class InterpreterError(RuntimeError):
    pass


class Environment:
    def __init__(self):
        self.vars = {}

    def get(self, name):
        if name not in self.vars:
            raise InterpreterError(f"Undefined variable '{name}'")
        return self.vars[name]

    def set(self, name, value):
        self.vars[name] = value


class Interpreter:
    def __init__(self):
        self.env = Environment()

    def interpret(self, node):
        if isinstance(node, Block):
            return self._eval_block(node)
        return self._eval(node)

    def _eval(self, node):
        if isinstance(node, Number):
            return node.value
        if isinstance(node, String):
            return node.value
        if isinstance(node, Ident):
            return self.env.get(node.name)
        if isinstance(node, Assign):
            val = self._eval(node.expr)
            self.env.set(node.name, val)
            return val
        if isinstance(node, BinOp):
            left = self._eval(node.left)
            right = self._eval(node.right)
            if node.op == "PLUS":
                if isinstance(left, str) or isinstance(right, str):
                    return str(left) + str(right)
                return left + right
            if node.op == "MINUS":
                return left - right
            if node.op == "MUL":
                return left * right
            if node.op == "DIV":
                return left / right
            if node.op == "GT":
                return left > right
            if node.op == "LT":
                return left < right
            if node.op == "EQ":
                return left == right
        if isinstance(node, Print):
            val = self._eval(node.expr)
            print(val)
            return val
        if isinstance(node, If):
            cond = self._eval(node.cond)
            if cond:
                return self._eval_block(node.body)
            return None
        if isinstance(node, Loop):
            count = self._eval(node.count)
            if not isinstance(count, (int, float)):
                raise InterpreterError("Loop count must be a number")
            result = None
            for _ in range(int(count)):
                result = self._eval_block(node.body)
            return result
        raise InterpreterError(f"Unknown node: {type(node).__name__}")

    def _eval_block(self, block):
        result = None
        for stmt in block.statements:
            result = self._eval(stmt)
        return result


def interpret(ast):
    Interpreter().interpret(ast)
