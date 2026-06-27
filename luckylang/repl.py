import sys
import os
from . import run

class LuckylangREPL:
    def __init__(self):
        self.env = {}
        self.history_file = ".luckylang_history"
        self.history = []
        self.in_block = False
        self.block_indent_level = 0
        
    def load_history(self):
        if os.path.exists(self.history_file):
            with open(self.history_file, 'r') as f:
                self.history = [line.rstrip('\n') for line in f.readlines()]
    
    def save_history(self):
        with open(self.history_file, 'w') as f:
            for line in self.history:
                f.write(line + '\n')
    
    def indent_size(self, line):
        return len(line) - len(line.lstrip())
    
    def format_prompt(self):
        if self.in_block:
            return "... "
        return "lukylang> "
    
    def execute_line(self, line):
        if not line:
            return False
            
        self.history.append(line)
        
        if line in ("exit", "quit", ":q", ":quit"):
            print("Goodbye!")
            sys.exit(0)
            
        if line == ":clear":
            import os
            os.system("cls" if os.name == "nt" else "clear")
            return True
            
        if line == ":help":
            self.show_help()
            return True
            
        if line == ":history":
            self.show_history()
            return True
            
        if line == ":save":
            self.save_history()
            print("✓ History saved")
            return True
            
        try:
            run(line)
            return True
        except Exception as e:
            print(f"✗ Error: {e}")
            return False
    
    def show_help(self):
        help_text = """
====== Lukylang REPL Commands ======
:help              Show this help message
:clear             Clear the screen
:history           Show command history
:save              Save history to .luckylang_history
:quit/:q           Exit the REPL

====== Lukylang Syntax ======
print "Hello World"
x = 10
if x > 5 {
    print "x is big"
}
fn name() {
    return "value"
}
==============================
"""
        print(help_text)
        
    def show_history(self):
        print("\n====== Command History ======")
        for i, cmd in enumerate(self.history[-20:], 1):
            print(f"{i}. {cmd}")
        print()
        
    def check_block_complete(self, line, block_started):
        stripped = line.strip()
        if not stripped:
            return block_started, line
            
        if stripped.endswith('{') and not stripped.endswith('}'):
            return True, line
            
        if self.in_block:
            if block_started:
                current_indent = self.indent_size(line)
                if current_indent > self.block_indent_level and stripped:
                    return True, line
                elif stripped.endswith('}'):
                    return False, line
                else:
                    return True, line
            elif stripped.endswith('}'):
                return False, line
        return block_started, line
        
    def show_examples(self):
        print("\n====== Example Programs ======")
        examples = """
print "Hello from Lukylang!"

x = 10
if x > 5 {
    print "x is greater than 5"
}

fn greet(name) {
    return "Hello " + name
}
print greet("World")

nums = [1, 2, 3]
print "List: " + nums
nums.append(4)
print "After append: " + nums

person = {"name": "Alice", "age": 30}
print "Age: " + person["age"]
person["age"] = 31
print "Updated age: " + person["age"]
"""
        print(examples)
    
    def run(self):
        print("╔══════════════════════════════════════╗")
        print("║  Lukylang Interactive REPL           ║")
        print("║  Type :help for commands             ║")
        print("║  Type :quit or Ctrl+D to exit       ║")
        print("╚══════════════════════════════════════╝\n")
        
        self.load_history()
        self.show_examples()
        
        while True:
            try:
                line = input(self.format_prompt()).rstrip()
                
                if line in ("": "exit", "quit", ":q", ":quit"):
                    if line in ("exit", "quit", ":q"):
                        print("Goodbye!")
                        break
                    continue
                    
                in_block_before = self.in_block
                self.in_block, processed_line = self.check_block_complete(line, self.in_block)
                
                if in_block_before != self.in_block:
                    self.block_indent_level = self.indent_size(line) if line.strip() else 0
                
                if not self.execute_line(processed_line):
                    pass
                    
            except KeyboardInterrupt:
                print("\nInterrupted! Press Enter to continue...")
                input()
                continue
            except EOFError:
                print("\nGoodbye!")
                break
                
        self.save_history()
    
    def commands():
        help_text = """
====== Common REPL Commands ======
:help              Show this help
:clear             Clear screen
:quit/:q           Exit
:history           Show previous commands
:save              Save history to file

====== Tips ======
- Use :help for available commands
- Press Ctrl+D to exit
- Type a complete statement and press Enter
- Use multi-line blocks for { }
==============================
"""
        return help_text


def main():
    repl = LuckylangREPL()
    repl.run()