# Luckylang 2.0 — Blueprint Plan

**Objective**: Transform Luckylang from a toy interpreter into a usable scripting language with functions, data structures, standard library, REPL, and module system.

**Repository**: `C:\Users\hp\luckylang`
**Current state**: Basic interpreter (lexer → parser → interpreter) with variables, print, if, loop, arithmetic.

---

## Phase 1 — Core Language Features (Steps 1–6)

### Step 1: Functions — Definition, Call, Return
**Files**: `luckylang/parser.py`, `luckylang/interpreter.py`, `luckylang/lexer.py`  
**Syntax**:
```lucky
fn add(a, b) {
    return a + b
}
result = add(5, 3)
print result
```
**Changes**:
- Lexer: add `FN`, `RETURN`, `COMMA`, `LPAREN`, `RPAREN` tokens
- Parser: `parse_fn_def`, `parse_call`, `parse_return`
- Interpreter: `Function` object, `CallFrame` for call stack, `ReturnException` for early return
**Verify**: `examples/functions.lucky` runs, recursion works (factorial)

---

### Step 2: Data Structures — Lists and Dicts
**Files**: `luckylang/parser.py`, `luckylang/interpreter.py`, `luckylang/lexer.py`  
**Syntax**:
```lucky
nums = [1, 2, 3]
nums.append(4)
print nums[0]        # 1
print len(nums)      # 4

person = {"name": "Lucky", "age": 25}
print person["name"]
person["age"] = 26
```
**Changes**:
- Lexer: `LBRACKET`, `RBRACKET`, `COLON`
- Parser: `parse_list`, `parse_dict`, `parse_index`, `parse_method_call`
- Interpreter: `List` and `Dict` classes with methods, index assignment
**Verify**: `examples/lists_dicts.lucky` runs

---

### Step 3: String Interpolation
**Files**: `luckylang/lexer.py`, `luckylang/parser.py`, `luckylang/interpreter.py`  
**Syntax**:
```lucky
name = "Lucky"
print f"Hello {name}!"
print f"2 + 2 = {2 + 2}"
```
**Changes**:
- Lexer: detect `f"` prefix, parse interpolation expressions inside `{}`
- Parser: `parse_interpolated_string` → list of (string | expr) parts
- Interpreter: evaluate parts, concat
**Verify**: `examples/interpolation.lucky` runs

---

### Step 4: Comparison & Logical Operators
**Files**: `luckylang/lexer.py`, `luckylang/parser.py`, `luckylang/interpreter.py`  
**Operators**: `==`, `!=`, `>=`, `<=`, `>`, `<`, `and`, `or`, `not`  
**Changes**:
- Lexer: add tokens
- Parser: extend precedence (comparison < logical < arithmetic)
- Interpreter: implement short-circuit `and`/`or`, truthiness for all types
**Verify**: `examples/logic.lucky` runs

---

### Step 5: Comments
**Files**: `luckylang/lexer.py`  
**Syntax**: `# comment` and `// comment` (single-line)  
**Changes**: Add to `SKIP` patterns in lexer
**Verify**: comments ignored in `examples/comments.lucky`

---

### Step 6: Better Errors — Line/Column Tracking
**Files**: `luckylang/lexer.py`, `luckylang/parser.py`, `luckylang/interpreter.py`, `luckylang/errors.py` (new)  
**Changes**:
- Token carries `line`, `col`
- Parser errors include position
- Interpreter errors show source snippet with `^` marker
- Custom exception hierarchy: `LexError`, `ParseError`, `RuntimeError`
**Verify**: `python main.py examples/error.lucky` shows helpful message

---

## Phase 2 — Standard Library (Steps 7–9)

### Step 7: Built-in Functions
**Files**: `luckylang/stdlib.py` (new), `luckylang/interpreter.py`  
**Functions**: `len`, `print`, `input`, `int`, `str`, `float`, `range`, `type`  
**Changes**:
- `stdlib.py`: `BUILTINS = {"len": builtin_len, ...}`
- Interpreter: pre-populate global env with `BUILTINS`
- `range(n)` returns list `[0..n-1]`
**Verify**: `examples/builtins.lucky` runs

---

### Step 8: List & Dict Methods
**Files**: `luckylang/stdlib.py`, `luckylang/interpreter.py`  
**List**: `append`, `pop`, `index`, `insert`, `remove`, `clear`  
**Dict**: `keys`, `values`, `get`, `pop`, `update`, `clear`  
**Changes**: Method dispatch in interpreter, bind methods to list/dict instances
**Verify**: `examples/methods.lucky` runs

---

### Step 9: Math Module
**Files**: `luckylang/stdlib.py`  
**Functions**: `abs`, `min`, `max`, `sum`, `round`, `pow`  
**Changes**: Add to `BUILTINS` or separate `math` module
**Verify**: `examples/math.lucky` runs

---

## Phase 3 — Tooling (Steps 10–12)

### Step 10: REPL Mode
**Files**: `luckylang/repl.py` (new), `main.py`  
**Features**:
- Persistent environment across lines
- Multi-line input for blocks (detect unclosed `{`)
- History (up/down arrows)
- `:help`, `:quit`, `:clear` commands
**Changes**: New entry point in `main.py` when no args or `--repl`
**Verify**: `python main.py --repl` works interactively

---

### Step 11: Module/Import System
**Files**: `luckylang/parser.py`, `luckylang/interpreter.py`, `luckylang/loader.py` (new)  
**Syntax**:
```lucky
import "utils"
import "math" as m
utils.helper()
m.sqrt(16)
```
**Changes**:
- Parser: `parse_import`
- Loader: resolve path, read file, parse, interpret in new env, return module dict
- Interpreter: `Import` node, cache loaded modules
**Verify**: `examples/import.lucky` + `examples/modules/utils.lucky`

---

### Step 12: CLI Polish
**Files**: `main.py`  
**Flags**: `--version`, `--help`, `--repl`, `--file <path>`, `--debug` (AST dump)  
**Changes**: Use `argparse`, clean help text, version from `__version__`
**Verify**: All flags work, `python main.py --help` shows usage

---

## Phase 4 — Quality & Docs (Steps 13–15)

### Step 13: Test Suite
**Files**: `tests/test_lexer.py`, `tests/test_parser.py`, `tests/test_interpreter.py`, `tests/test_stdlib.py`, `tests/test_integration.py`, `pytest.ini`  
**Framework**: `pytest`  
**Coverage**: Unit tests per module + integration tests per example file  
**Target**: ≥80% coverage  
**Verify**: `pytest -v` passes

---

### Step 14: Documentation
**Files**: `docs/language.md`, `docs/stdlib.md`, `docs/cli.md`, `docs/examples.md`  
**Content**: Language reference, stdlib API, CLI guide, example programs  
**Verify**: `docs/` renders on GitHub Pages

---

### Step 15: CI/CD
**Files**: `.github/workflows/ci.yml`  
**Jobs**: lint (ruff), type-check (mypy), test (pytest), build docs  
**Trigger**: push, PR  
**Verify**: Green check on GitHub Actions

---

## Dependency Graph

```
1 (functions) ────┐
                  ├──→ 2 (lists/dicts) ──→ 3 (interpolation)
2 (lists/dicts) ──┤                          │
                  ├──→ 4 (operators) ────────┤
                  ├──→ 5 (comments)          │
                  └──→ 6 (errors) ───────────┤
                                              ├──→ 7 (builtins) ──→ 8 (methods) ──→ 9 (math)
                                              │
                                              ├──→ 10 (repl)
                                              ├──→ 11 (import) ──────→ 12 (cli)
                                              │
                                              └──→ 13 (tests) ──→ 14 (docs) ──→ 15 (CI)
```

**Parallel groups after Step 6**: {7,10,11} can run in parallel → {8,12} → {9,13} → 14 → 15

---

## Acceptance Criteria (Definition of Done)

- All example files in `examples/` run without error
- REPL starts and executes multi-line blocks
- `import` loads and caches modules
- Test suite passes with ≥80% coverage
- CI pipeline green on main branch
- Docs published and linked in README

---

## Mutation Protocol

If a step grows beyond ~400 lines of changes or takes >2 hours:
1. Split into sub-steps (e.g., 2a: lists, 2b: dicts)
2. Update this plan with new step IDs
3. Preserve dependency order