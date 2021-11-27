# To create tuple we use () these braces
fruits = ("apple", "orange", "mango")
print(fruits)
print(type(fruits))

# we can also create a tuple with tuple() constructor
with_con_tuple = tuple(("Books", "Movies", "Music"))
print(with_con_tuple)
print(type(with_con_tuple))

# in tuple we can not add  new item or remove existing item from tuple
# there is now append or pop method in tuple like list we saw on previous video

# to find the length of tuple we can use len function
print(f"Length of fruits tuple: {len(fruits)}")

# check tuple that allow duplicates values
dup_tuple = ("John", "Mike", "Tom", "Sara", "Tom")
print(dup_tuple)

# create a single item tuple
# but we have to pass , with the value
one_tuple_item = ("orange", )
print(type(one_tuple_item))
# if we do not pass , with the item than it will count as string not tuple
one_tuple_item = ("Orange")
print(type(one_tuple_item))