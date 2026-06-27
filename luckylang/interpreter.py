class Function:
    def __init__(self, name, params, body, env=None):
        self.name = name
        self.params = params
        self.body = body
        self.env = env or Environment()

    def __repr__(self):
        return f"<Function {self.name}>"


class InterpreterError(Exception):
    def __init__(self, message, line=0, col=0):
        super().__init__(f"Runtime Error at line {line}, col {col}: {message}")
        self.line = line
        self.col = col


class Environment:
    def __init__(self, parent=None):
        self.vars = {}
        self.parent = parent

    def get(self, name):
        if name in self.vars:
            return self.vars[name]
        elif self.parent:
            return self.parent.get(name)
        raise InterpreterError(f"Undefined variable '{name}'")

    def set(self, name, value):
        self.vars[name] = value


class CallFrame:
    def __init__(self, func, args, env):
        self.func = func
        self.args = args
        self.env = env
        self.pc = 0


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
            if node.op == "NE":
                return left != right
            if node.op == "GTE":
                return left >= right
            if node.op == "LTE":
                return left <= right
            if node.op == "AND":
                return bool(left) and bool(right)
            if node.op == "OR":
                return bool(left) or bool(right)
            if node.op == "NOT":
                return not bool(left)
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
                raise InterpreterError(f"Loop count must be a number, got {count}")
            result = None
            for _ in range(int(count)):
                result = self._eval_block(node.body)
            return result
        if isinstance(node, Function):
            return node
        if isinstance(node, Call):
            return self._call_function(node)
        if isinstance(node, Return):
            raise ReturnException(self._eval(node.expr) if node.expr else None)
        if isinstance(node, List):
            return [self._eval(item) for item in node.elements]
        if isinstance(node, Dict):
            result = {}
            for key, value in node.pairs:
                result[self._eval(key)] = self._eval(value)
            return result
        if isinstance(node, Index):
            obj = self._eval(node.obj)
            key = self._eval(node.index)
            if isinstance(obj, list):
                if not isinstance(key, int):
                    raise InterpreterError(f"List index must be integer, got {type(key)}")
                return obj[key]
            elif isinstance(obj, dict):
                if key not in obj:
                    raise InterpreterError(f"Key '{key}' not found in dict")
                return obj[key]
            else:
                raise InterpreterError(f"Cannot subscript {type(obj).__name__}")
        raise InterpreterError(f"Unknown node: {type(node).__name__}")

    def _eval_block(self, block):
        result = None
        for stmt in block.statements:
            result = self._eval(stmt)
        return result

    def _call_function(self, call):
        callee = self._eval(call.callee)
        if not isinstance(callee, Function):
            raise InterpreterError(f"Not a function: {callee}")
        args = [self._eval(arg) for arg in call.args]
        if len(args) != len(callee.params):
            raise InterpreterError(
                f"Function '{callee.name}' expected {len(callee.params)} "
                f"arguments, got {len(args)}"
            )
        new_env = Environment(callee.env)
        for param, arg in zip(callee.params, args):
            new_env.set(param, arg)
        try:
            result = self._eval_block(callee.body)
        except ReturnException as ret:
            result = ret.value
        return result


class ReturnException(Exception):
    def __init__(self, value):
        self.value = value


def interpret(ast):
    Interpreter().interpret(ast)