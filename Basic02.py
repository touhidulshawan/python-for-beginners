# string type

name = "Mike" # Here name is string (str) type
# we can check that with the help of type method
print(type(name))

# int type
num = 10 # This is int value
print(type(num))

# float type
float_number = 10.5 # This is float number
print(type(float_number))

# boolean type
# There are only type of bool 1. True & 2. False
is_raining = False
print(type(is_raining))
# We will see others data type later

# Now we will cast int data type to float data type

int_num = 15

float_num = float(int_num)
print(float_num)
print(f'Data type of float_number : {type(float_num)}')
