# Set is declared with {} these braces
fruit_set = {"Apple", "Mango", "Banana"}
print(fruit_set)
print(type(fruit_set))

# set does not allow duplicate items
fruit_set = {"Apple", "Mango", "Banana", "Apple"}
# does not show Apple twice
print(fruit_set)

# add new item in set
# fruit_set.add("Strawberry")
# print(fruit_set)

# Since set is not indexed we can not access it's items with previous sysntax

# we have to use for loop
# we will learn more about loop in future video

for fruit in fruit_set:
    print(fruit)

# remove a item

fruit_set.remove("Apple")

print(fruit_set)

# if remove does not find the given item than it will raise a exception

# fruit_set.remove("Apple")

# we can use discard to remove item
# remove Banana
fruit_set.discard("Banana")
print(fruit_set)

# if discard does not find give item than it will not raise a exception like
# remove

fruit_set.discard("Banana")
# no exception
