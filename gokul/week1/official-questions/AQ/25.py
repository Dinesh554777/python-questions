# Accept a positive integer as input and print True if it is a perfect square and False otherwise. For example, if the input is 25 , then you must print True . If the input is 15 , then you must print False

import math

num = int(input("Enter a positive integer: "))


root = math.isqrt(num)
if root * root == num:
    print("True")
else:
    print("False")