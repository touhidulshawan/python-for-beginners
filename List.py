# declare a list

fruits = ["apple", "mango", "banana", "orange"]
#            0         1        2       3
print(fruits)
print(type(fruits))

# access individual items on a list
# we can access a item with its index number. And in python index number start with 0
print(fruits[0]) # will print apple
print(fruits[3]) # will print orange

# we can also access item with for loop but will see that later.

# Change a list item
# Suppose we want to replace banana with strawberry How can we do that?
fruits[2] = "strawberry"
print(fruits)

# Add new items on list
# Here append method will add new item at the end of list
fruits.append("Coconut")
print(f"After adding new item: {fruits}")

# If we want to give specific position to insert new item than we can use inset method
fruits.insert(0, "Avacado")
print(fruits)

# Remove a item
# we can use pop to remove item
# pop will remove last item of the list and return it
pop_item = fruits.pop()
print(fruits)
print(pop_item)
# if we want to remove item and not want to return it than we can use remove
fruits.remove("mango")
print(fruits)
# So we saw that remove method only remove item that value is given and do not
# return it but it will give error if the given item is not in list
fruits.remove("mango")
