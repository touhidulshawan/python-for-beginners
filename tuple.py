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

# Access tuple item

my_tuple = ("Apple", "Mango", "Strawberry", "Banana")

# To access a item we can access with it's index number like we do in list
# print Banana
print(my_tuple[3])

# Update tuple
# In previous video we said that tuple is unchangeable then how can we update
# a tuple. We can change or update a tuple by converting into a list that we
# can update that list and convert updated list to tuple again
# first see that we can really change  a tuple item without this trick
# so  this is giving us an error that we can not update tuple item
# my_tuple[2] = "Orange"
# Now do the tricks
my_list = list(my_tuple)
print(my_list)
my_list[1] = "Orange"
my_tuple = tuple(my_list)
print(my_tuple)
# so  update the tuple we replace Mango with orange

# Join tuples

tuple_1 = ("Tom", "Mike", "John")
tuple_2 = (1, 4, 5, 6)
joined_tuple = tuple_1 + tuple_2
print(f"Joined tuple: {joined_tuple}")

# we can also double the tuple item

double_tuple = tuple_1 * 2
print(double_tuple)















