#!/usr/bin/env python3
"""Quick test to check if luckylang works"""

import sys
import os

# Add luckylang to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    # Test the core functionality
    print("=" * 60)
    print("LUCKYLANG INTERNAL TEST")
    print("=" * 60)
    
    # Test imports
    print("\n1. Testing core imports...")
    from luckylang.lexer import tokenize
    from luckylang.parser import Parser
    from luckylang.interpreter import Interpreter
    print("   ✅ All core modules imported successfully")
    
    # Test basic tokenization
    print("\n2. Testing basic tokenization...")
    tokens = tokenize("x = 10 + 5")
    print(f"   ✅ Generated {len(tokens)} tokens")
    for tok in tokens[:3]:
        print(f"      {tok.kind}: {tok.value}")
    
    # Test parsing
    print("\n3. Testing basic parsing...")
    parser = Parser(tokens)
    ast = parser.parse()
    print(f"   ✅ Parsed AST with {len(ast.statements)} statements")
    
    # Test interpretation
    print("\n4. Testing basic interpretation...")
    interpreter = Interpreter()
    result = interpreter.interpret(ast)
    print(f"   ✅ Execution completed")
    
    print("\n" + "=" * 60)
    print("SUCCESS: Luckylang core functionality works!")
    print("=" * 60)
    print("\nReady to continue with REPL functionality or other features?")
    
except Exception as e:
    print("\n❌ ERROR:")
    print(f"   {type(e).__name__}: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)