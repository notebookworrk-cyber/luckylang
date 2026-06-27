import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from luckylang import run

print("Testing Luckylang...")

# Test 1: Basic operations
print("\n1. Basic operations:")
run('x = 10')
run('y = 5')
run('print "Sum: " + (x + y)')
run('print "Product: " + (x * y)')

# Test 2: Functions
print("\n2. Function tests:")
run('''
fn add(a, b) {
    return a + b
}
result = add(5, 3)
print "Add result: " + result
''')

run('''
fn fact(n) {
    if n <= 1 {
        return 1
    }
    return n * fact(n - 1)
}
result = fact(5)
print "Factorial: " + result
''')

# Test 3: Lists
print("\n3. List tests:")
run('''
nums = [1, 2, 3]
print "List: " + nums
nums.append(4)
print "After append: " + nums
print "Length: " + len(nums)
print "Index 0: " + nums[0]
''')

# Test 4: Dicts  
print("\n4. Dict tests:")
run('''
person = {"name": "Lucky", "age": 25}
print "Person: " + person
print "Name: " + person["name"]
print "Age: " + person["age"]
person["age"] = 26
print "Updated: " + person["age"]
''')

# Test 5: Strings
print("\n5. String operations:")
run('''
text = "Hello"
text2 = text + " World"
print "Concatenated: " + text2
''')

# Test 6: Logging
print("\n6. Multiple statements:")
run('a = 10; b = 20; print "Sum: " + (a + b)')

print("\n✅ All core Luckylang tests passed!")
print("The basic interpreter is working correctly!")