# 1. what is dynamic typing?

"""Dynamic typing is a programming language feature where variable data types are evaluated and assigned at runtime rather than at compile time"""

# 1. Variable holds an integer
data = 10
print(type(data))  # Output: <class 'int'>

# 2. Same variable changes to a string without errors
data = "Hello World"
print(type(data))  # Output: <class 'str'>

# 3. Same variable now holds a list
data = [1, 2, 3]
print(type(data))  # Output: <class 'list'>
