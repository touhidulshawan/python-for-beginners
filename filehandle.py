# file = open("test.txt", "r")
#
# print(file.read())
#
# # we can also print line by line
# # with readline
#
# print(file.readline())
# print(file.readline())
#
# for f in file:
#     print(f)
#
# # to close file we use close method
#
# file.close()

# we can use open with another way to read file

# now will  use w flag to write into the file
# with open("test.txt", 'w') as file:
#     file.write("I have learned how to read file")
#     file.close()

# # using a flag
# with open("test.txt", "a") as file:
#     file.write("\nHello! This content will append with previous content.")
#     file.close()

# with open('test2.txt', "x") as file:
#     file.write("This is new file")
#     file.close()


# with open("withw.txt", "w") as file:
#     print(file)
#
# create a new file

# with open("witha.txt", "a") as file:
#     print(file)
