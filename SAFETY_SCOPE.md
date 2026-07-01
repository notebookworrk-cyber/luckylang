> **⚠️ ARCHIVED:** Merged into [zoya-easy-code](https://github.com/notebookworrk-cyber/zoya-easy-code). See that repository for the active project.

# Luckylang 2.0 SAFETY Scope Refinement

## Current State
- ✅ Luckylang interpreter: lexer→parser→interpreter working
- ✅ Basic operations: variables, print, if, loop
- ✅ String/numeric operations (concatenation, arithmetic)
- ❌ GitHub user expects REAL 2.0 experience, not toy

## Refined Priorities (6 High-Impact Features)

### Phase 1 (Must-Have - Terminal)

#### 1️⃣ Functions & Returns (core")
- [ ] `fn add(a, b) { return a + b }`
- [ ] `result = add(5, 3)`
- [ ] `fact(5)` with local scope
- Impact: Makes code reuse possible

#### 2️⃣ Data Structures (usability")  
- [ ] Lists: `[1, 2, 3]`, `.append()`, `nums[0]`
- [ ] Dicts: `{"name": "Lucky"}`, `person["age"] = 26`
- Impact: Real-world data handling

#### 3️⃣ REPL Mode (interactive")
- [ ] `python main.py --repl` or `python main.py -r`
- [ ] `x = 10` (multi-line blocks)
- [ ] `:quit`, `:clear`, `:help`
- Impact: Developer experience jump

### Phase 2 (Should-Have - Differentiation)

#### 4️⃣ Module System (scoping")
- [ ] `import "utils"`
- [ ] Alias: `import "math" as m`
- [ ] Relative imports

#### 5️⃣ Better Errors (debugging")
- [ ] Syntax: "Parse Error at line 3, col 10: Unexpected 'x'"
- [ ] Runtime: "Runtime Error at line 7: Division by zero"
- [ ] Highlight error source in source

#### 6️⃣ Documentation (learning")
- [ ] `python main.py --help` - Usage
- [ ] `python main.py --version` - Version
- [ ] README.md examples

## What We DON'T Do Yet:
- ❌ String interpolation f"{var}"
- ❌ Comparisons (>, <, >=, <=)
- ❌ Logical operators (&&, ||, !)
- ❌ Full stdlib (math, input, etc.)
- ❌ CI/CD automation
- ❌ Comprehensive tests (table stakes, not differentiator)

## WHY This Matters:
1. **Functions + Data** = Code you can actually reuse
2. **REPL** = Interactive development
3. **Modules** = Organizable projects
4. **Errors** = Survive debugging sessions
5. **Docs** = Actually usable by others

## Scopes:

**DELIVERY MODE:** What's the minimal 2.0 we can ship that feels like a real language?
- Functions + Lists + REPL + Modules + Errors + Docs

**FINAL MODE:** What can we build in 2-3 iterations?
- Everything from above PLUS vs interpolation, all comparisons, full stdlib, CI/CD

The user wants 2.0 - this is the "just barely functional 2.0" that's game-changing vs the original toy version.