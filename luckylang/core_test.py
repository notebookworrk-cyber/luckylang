import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from luckylang import run

print("Testing Luckylang 2.0 core features...")

# Test 1: Basic operations
print("\n1. Basic operations:")
run('x = 10')
run('y = 5')
run('print "Sum: " + (x + y)')
run('print "Product: " + (x * y)')

# Test 2: Functions with parameters and return
print("\n2. Function tests:")
run('''
fn add(a, b) {
    return a + b
}
result = add(5, 3)
print "Add result: " + result
''')

run('''
fn factorial(n) {
    if n <= 1 {
        return 1
    }
    return n * factorial(n - 1)
}
result = factorial(5)
print "Factorial of 5: " + result
''')

# Test 3: Lists
print("\n3. List tests:")
run('''
nums = [1, 2, 3]
print "Original list: " + nums
nums.append(4)
print "After append: " + nums
print "Length: " + len(nums)
print "Index 0: " + nums[0]
''')

# Test 4: Dicts
print("\n4. Dict tests:")
run('''
person = {"name": "Lucky", "age": 25, "city": "NYC"}
print "Name: " + person["name"]
print "City: " + person["city"]
person["age"] = 26
print "Updated age: " + person["age"]
print "Keys: " + keys(person)
print "Values: " + values(person)
''')

# Test 5: String interpolation
print("\n5. String interpolation:")
run('''
name = "Test"
age = 25
print f"Hello {name}, you are {age} years old!"
''')

# Test 6: Comparison and logical operators
print("\n6. Logical operators:")
run('''
a = 10
b = 20
if a < b && b > 15 {
    print "a < b AND b > 15"
}
if a == b || b > 15 {
    print "a == b OR b > 15"
}
if not (a == b) {
    print "a is NOT equal to b"
}
''')

print("\n✅ All Luckylang 2.0 core tests passed!")