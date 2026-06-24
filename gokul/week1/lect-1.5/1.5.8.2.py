# Note the different types of formatting, try running this.

txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)

print(txt1)
print(txt2)
print(txt3)
txt4 ="My name is {fname}, I'm {age} yeard old".format(fname="Dinesh", age=20)
txt5="My name is {0}, I'm {1} years old".format("Dinesh",20)
print(txt4)
print(txt5)