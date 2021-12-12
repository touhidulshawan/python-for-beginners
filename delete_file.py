import os

# os.remove("witha.txt")

# if we do not check then this code will give error
# now add some condition to check file exist or not
# if exist then delete otherwise print a message

if os.path.exists('test2.txt'):
    os.remove("test2.txt")
    print("File delete successfully")
else:
    print("File not found.")
