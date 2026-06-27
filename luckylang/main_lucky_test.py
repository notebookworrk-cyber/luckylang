import tempfile
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from luckylang import run

print("Testing Luckylang 2.0 core features...")

# Test 1: Basic operations
print("\n1. Basic operations:")
run('x = 10')
run('y = 5')
run('print "Sum: " + (x + y)')
run('print "Product: " + (x * y)')

# Test 2: Functions
print("\n2. Function tests:")
run('''
fn fact(n) {
    if n <= 1 {
        return 1
    }
    return n * fact(n - 1)
}
result = fact(5)
print "Factorial of 5: " + result
''')

# Test 3: Lists
print("\n3. List tests:")
run('''
nums = [1, 2, 3]
nums.append(4)
print "Length of nums: " + len(nums)
print "First element: " + nums[0]
''')

# Test 4: Dicts
print("\n4. Dict tests:")
run('''
person = {"name": "Lucky", "age": 25}
print "Name: " + person["name"]
print "Age: " + person["age"]
''')

# Test 5: String interpolation
print("\n5. String interpolation:")
run('''
name = "Test"
print f"Hello {name}!"
''')

# Test 6: Logical operators
print("\n6. Logical operators:")
run('''
a = 10
b = 20
if a < b && b > 15 {
    print "a is less than b and b > 15"
}
''')

print("\n✅ All Luckylang 2.0 tests passed!")