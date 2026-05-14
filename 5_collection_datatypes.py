# Collections:

    # List:-
        # List is a collection datatype
        # List is heterogeneous datatype [it can contain variety of data]
        # List is ordered collection
        # List supports indexing
        # List is mutable datatype  [can be modified after its initialization]
        # List can contain duplicates

# How to create a list ?

    # using []
    # using list()

# list1 = [1, 2, 3, 4, 5.5, 1, 'Hello']
# print(list1)
# print(type(list1))  # list

# print(list1[4])
# print(list1[-3])

# print(list1[-1])
# print(list1[6])

# Nested Indexing
# print(list1[6][1])
# print(list1[6][-4])

# lle
# print(list1[-1][-2:-5:-1])

# list in-built methods:

    # Inserion Methods:
# list11 = [12, "A", 5.5, 2, 4+6j]

# .append()  # append method is used to insert element at the end of the list
# list11.append(6)
# print(list11)

# .extend()  # adds multiple elements the end of list (elements must be in the form of iterable)
# list11.extend([12, 23, 34])
# list11.extend(("M", 12, 'Hello'))
# list11.extend({90, 3.3, "W"})
# print(list11)

# list12 = [1, 2.2, 3-4j,'H', [0, 'S', 5]]

# .insert() # To add element at specific index inser is used
# list12.insert(0, "Trump")
# list12.insert(2, 45)

# -------------- List methods for delition
# .remove()  # removes specified element from list if avialable

# list13 = [1, 2, 3, 4, 5]
# list13.remove(4)
# list13.remove(1)
# # list13.remove(100)  #ValueError: list.remove(x): x not in list 
# print(list13)

# .pop()  # removes last element of the list
# list13.pop()
# list13.pop()
# print(list13)

# list13.pop(1)
# print(list13)

# .clear()  # it removes all elements from the list
# list13.clear()
# print(list13)  #[]

# l1 = [11, 22, 33]
# l2 = l1
# l1[0] = 100

# print(l1, id(l1))
# print(l2, id(l2))
# l2 = l1.copy()
# l1[0] = 1000
# print(l1, id(l1))
# print(l2, id(l2))

# l1 = [11, 22, 33, ["A","B", "C"]]
# l2 = l1.copy()
# l1[3][0] = 'Z'

# print(l1, id(l1))
# print(l2, id(l2))
# import copy

# l1 = [11, 22, 33, [1, 2, 3]]
# l2 = copy.deepcopy(l1)
# l1[3][0] = 1000

# print(l1, id(l1))
# print(l2, id(l2))

#----------------------------------

# list100 = ["A", "B", "C", "D"]
# print(list100.index("A"))


    # Tuple:-
        # Tuple is also collection datatype
        # Tuple is also heterogeneous in nature
        # Tuple is also ordered
        # Tuple supports indexing
        # Tuple is immutable [cant be modified ever after initialization]
        # Tuple also can contain duplicates

# How to create tuple ?
    # using ()
    # using tuple()

# tup1 = ()
# print(tup1)
# print(type(tup1))

# tup2 = (1, 2, 3, 4, 6.6, "Helo")
# print(tup2)
# print(type(tup2))

# tup3 = tuple([12, 23, 34])
# print(tup3)
# print(type(tup3))

# tup4 = (("A", "B", 1, 2.2))
# print(tup4)
# print(type(tup4))

#---------------------------------

# tup5 = (12, 34, 45, 56, 67, 7, 8)
# print(tup5[3])
# print(tup5[-4])
# print(tup5[2:5:1])
# print(tup5[-5:-2:1])
# # ---------------------
# print(tup5[-3:-6:-1])

#---------------------Built-in Methods
# .count()
# tup6 = (1, 2, 3, 4, 1, 2, 1, 1, 1, 5, 6, 7, 8)
# print(tup6.count(1))
# print(tup6.count(2))

# # .index()
# print(tup6.index(3))
# print(tup6.index(8))


    # Set:-
        # Set is also a collection dataype
        # Set is partially heterogeneous [only immutable data]
        # Set itself is mutable
        # Set is unorderd 
        # Set doest support indexing
        # Set doesnt allow duplicates

# How to create the set.
    # using {}
    # using set()

# set1 = {1, 2, 3, 4, 5, 6}
# print(set1)
# print(type(set1))

# set2 = {"A"}
# print(set2)
# print(type(set2))

# set3 = set([12, 23, 3, 4])
# print(set3)
# print(type(set3))

#--------------------------------

# set4 = {1, 2, 1, 4, 5, 61, 1}
# print(set4)

# set5 = {True, 2, 0, 22, 1, False}
# print(set5)
# print(type(set5))


# ----------------- Built-In Methods on Set:

# set1 = {12, 23, 34, 45, 56}
# set1.add(67)

# set1.update(["A", "B", "C"])
# print(set1)

# set1.remove(67)
# print(set1)
# set1.pop()
# print(set1)

#-----------------------

# OPerations on set

set1 = {1, 2, 3, 4}
set2 = {4, 5, 6, 7}

# union
# set3 = set1 | set2
# set3 = set1.union(set2)
# print(set3)  #{1, 2, 3, 4, 5, 6, 7}

# difference  => all set1 elements which are not available in set2 
                # will be available in new set
# set4 = set1 - set2
# print(set4)

# set5 = set2 -set1
# print(set5)
# set5 = set1.difference(set2)
# set4 = set2.difference(set1)
# print(set4)
# print(set5)

# intersection ==> common elements from both the sets

# set6 = set1 & set2
# set7 = set1.intersection(set2)
# set8 = set2.intersection(set1)

# print(set6)
# print(set7)
# print(set8)

#------------------------

# s1 = {1, 2, 3, 4}
# s2 = {3, 4, 5, 6}

# s3 = s1.symmetric_difference(s2)
# print(s3)

# s1.symmetric_difference_update(s2)

# print(s1)
# print(s2)

#---------------------------

# superset
# subset

# s1 = {1, 2 ,3, 4, 5, 6}
# s2 = {3, 6, 10}

# print(s1.issuperset(s2))
# print(s2.issubset(s1))
