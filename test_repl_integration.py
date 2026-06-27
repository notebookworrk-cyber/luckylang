import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from luckylang.repl import LuckylangREPL

print("Testing Lukylang REPL...")
print("1. Testing basic import")
print("2. Testing REPL instantiation")
print("3. Testing help display")

repl = LuckylangREPL()
print("4. REPL instance created")

print("\n5. Help text preview:")
help_text = repl.commands()
print(help_text[:200] + "...")

print("6. Testing show_examples()")
repl.show_examples()

print("\n✅ REPL integration test completed!")