# How to create dictionary
student = {"id": 25, "name": "John Smith", "class": "Major is CS"}
# This is a dictionary.
# now see which is key and which is value
# print(student.keys())
# print(student.values())
# How to access dictionary item
print(student["name"])
# also we can use get()
print(student.get("class"))
# get items
print(student.items())
# How to change item
student["name"] = "Sara Smith"
print(student)
# also we can use update() method to update dictionary
student.update({"class": "Data Science"})
print(student)

# check if dictionary support duplicate or not
car = {
    "model": "Mustang",
    "brand": "Ford",
    "year": 1964,
    "is_available": False,
    # "brand": "Volvo",
}
print(car)
# take the latest value. not allow duplicate
# How to add new item
student.update({"hair": "Black"})
print(student)
# How to remove item
# There are 3 method with remove
# pop, popitem, del
# pop remove the specified item
student.pop("class")
print(student)
# class is gone

# popitem removes last inserted item of dictionary
student.popitem()
print(student)

# del remove specified item with keyname
del student["id"]
print(student)
