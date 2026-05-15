# Dictionary:
    # Dictionary is a collection of key and value pairs.
    # Dictionary is ordered
    # but indexed using its keys
    # In Dictionary keys must be unique
    # Dictionary is mutable 

# How to create a dictionary ?

    # using {}
    # using dict()

# dict1 = {}
# print(dict1)
# print(type(dict1))  # dict

# dict2 = {1:1, 2:4, 3:9, 4:16, 5:25}
# print(dict2)
# print(type(dict2))

#------------------
# l1 = ['A', "B", "C", "D", "E"]
# l2 = [65, 66, 67, 68]

# dict3 = dict(zip(l1, l2))
# print(dict3)

#-------------------------
# students = ["Gayathri", 'Vinod', "Mallesh"]
# dict4 = dict.fromkeys(students, "Failed")
# print(dict4)

#-------------------------

# dict5 = dict([("A", "B"), ("C", "D"), ("E", "F")])
# print(dict5)

#------------------------


# Indexing On Dictionary:

employees = {"emp1001": "Kumar Sanu", "emp1002": "Ravi Kishan", "emp1003": "Narendra Modi", "emp1004": "Donald Trump"}
# print(employees)

# access the name of employees whose employee Id is "emp1002"
# print(employees["emp1002"])
# print(employees["emp1004"])

# employees["emp1005"] = "Sachin Tendulkar"
# print(employees)

#----------------------------

# fruits = {"Apple": ["Green", "Red", "Yellow"], "Grapes": ["Yellow", "Green", "Pink", "Black"]}
# print(fruits["Apple"])
# print(fruits["Grapes"][0][0])

#-------------------

# In-Built Methods of Dictionary:

dict6 = {'Allan': 67, "Garry": 88, "Sara": 98, "David":65}

# keys :
# print(list(dict6.keys()))

# values:
# print(list(dict6.values()))

#----------------
# .popitems()  # last key-value pair
# dict6.popitem()
# print(dict6)

# .pop()  # can remove key-value pair using specified key
# dict6.pop("Garry")
# print(dict6)

# .clear()
# dict6.clear()
# print(dict6)

#------------------------------

# print(dict6.get("Garry"))

# print(list(dict6.items()))

#-------------------------------------------

dict_cities = {
    "Telangana": "Hyderabad", 
    "Andhra": "Amaravati", 
    "Tamilnadu": "Chennai", 
    "Maharashtra": "Mumbai"
    }
# Iannehc
# print(tuple(dict_cities.values())[2][::-1].title())
# print(dict_cities["Tamilnadu"][::-1].title())

# print(dict_cities["Andhra"])
# print(tuple(dict_cities.values()))

# print(set(dict_cities.keys()))
# VATINADU 
# print(dict_cities["Andhra"][5::].upper()+list(dict_cities.keys())[2][5::].upper())


# employees = {
#     "HR" : ["A", "B", "C"],
#     "Sales": ["Z", "M"]
# }