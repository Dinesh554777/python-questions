# L2.3: Variables Revisited: Dynamic Typing
- https://youtu.be/2OFZY77eOjw

1. predict the output
    ```
    a=10
    print(type(a))
    a="India"
    print(type(a))
    a=a+a
    print(a)
    ```
<class 'int'>
<class 'str'>
IndiaIndia

1. what is dynamic typing?
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

1. guess the output
    ```
    n=10
    print(type(n))
    print(n)
    n=n/2
    print(type(n))
    print(n)
    <class 'int'>
10
<class 'float'>
5.0