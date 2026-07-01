> **⚠️ ARCHIVED:** Merged into [zoya-easy-code](https://github.com/notebookworrk-cyber/zoya-easy-code). See that repository for the active project.

# Lukylang

Lukylang is a simple, educational programming language designed for learning and scripting.

## Getting Started

### Installation

Lukylang is distributed as a Python package:

```bash
pip install lukylang
```

### Basic Usage

From the command line:

```bash
# Run a Lukylang script
lukylang examples/hello.lucky

# Start interactive REPL
lukylang --repl

# Show help
lukylang --help

# Show version
lukylang --version

# Show examples
lukylang --examples
```

### REPL Commands

While in the REPL (`lukylang --repl`):

- `:help` - Show this help message
- `:clear` - Clear the screen
- `:quit` or `:q` - Exit the REPL
- `:history` - Show command history
- `:save` - Save history to file

## Example Programs

### Hello World

```lukylang
print "Hello, World!"
```

### Basic Operations

```lukylang
x = 10
y = 5
print "Sum: " + (x + y)
print "Product: " + (x * y)
```

### Functions

```lukylang
fn greet(name) {
    return "Hello, " + name
}

result = greet("World")
print result
```

### Conditionals

```lukylang
age = 18

if age >= 18 {
    print "Adult"
} else {
    print "Child"
}
```

### Loops

```lukylang
loop 3 {
    print "Iteration"
}
```

### Lists

```lukylang
nums = [1, 2, 3]
print "List: " + nums
nums.append(4)
print "After append: " + nums
print "Length: " + len(nums)
print "First element: " + nums[0]
```

### Dictionaries

```lukylang
person = {"name": "Alice", "age": 30}
print "Name: " + person["name"]
print "Age: " + person["age"]
person["age"] = 31
print "Updated age: " + person["age"]
```

## Syntax Reference

### Data Types

- **Numbers**: `10`, `3.14`
- **Strings**: `"hello"`, `"world"`
- **Lists**: `[1, 2, 3]`, `["a", "b"]`
- **Dictionaries**: `{"key": "value"}`, `{"name": "Alice"}`

### Operators

- **Arithmetic**: `+`, `-`, `*`, `/`
- **Comparison**: `>`, `<`, `>=`, `<=`, `==`, `!=`
- **Logical**: `and`, `or`, `not`
- **String Concatenation**: `+` (between strings)

### Control Flow

- **Conditionals**: `if`, `else`
- **Loops**: `loop`
- **Blocks**: `{ }` (for grouping statements)

## Features

### Core Language

- ✅ Variables and assignments
- ✅ Basic operators (arithmetic, comparison, logical)
- ✅ Functions with parameters and return values
- ✅ Conditional statements
- ✅ Loops
- ✅ Lists with methods (append, index, length)
- ✅ Dictionaries with key access and methods

### Developer Experience

- ✅ Interactive REPL with history
- ✅ Comprehensive error messages with line numbers
- ✅ Module/import system
- ✅ Command-line interface with flags
- ✅ Documentation and examples

## Development

### Running Tests

```bash
# Run all tests
pytest

# Run specific tests
pytest tests/test_interpreter.py
```

### Building

```bash
python -m pip install -e .
```

### Running REPL

```bash
lukylang --repl
```

## Community

- **GitHub**: https://github.com/notebookworrk-cyber/luckylang
- **Issues**: Report bugs and request features
- **Discussions**: Share ideas and get help

## License

This project is licensed under the MIT License.