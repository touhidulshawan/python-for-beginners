a = 15
b = 10
c = 5

# here if a is less than b than it will print the message. otherwise it will
# not print the message

if a < b:
    print("a is less than b")
elif a == b:
    print("a is equal b")
else:
    print('a is not less than b')

# and or in condition

# and

# in case of and both condition have to True

if a < b and a == c:
    print("Correct")
else:
    print("Not correct")

# or

# in case of  or one condition will be true than it will execute the code
if a > b or a == c:
    print("Correct")
else:
    print("Not correct")
