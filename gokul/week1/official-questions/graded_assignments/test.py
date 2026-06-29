print(type(1+4/2))
print(type(1 >0 and -1 < 0 and 1==1 ))
print(1+((3/(4**2))*0))
print((10**3) + (9**3) == (12**3) + (1**3)==1729)
E_1 = True
E_2 = False

E_3 = not (E_1 or E_2)
E_4 = (not E_1) and (not E_2)

print(E_3 == E_4)

E = False  # Our discovered answer


line_500_result = eval("not " * 500 + "E")

print("Line 500 evaluates to:", line_500_result)

# e1=True
# e2=True
# e1 and e2 and 1/0
# print(e2)