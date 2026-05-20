# Comprhensions:-

    # What is comprehesions:-
        # it is a form of collection where program is written.
        # that program generates data / elements


    # Comprehesions are easy write and read
    # Comprehensions are aslo easy to maintain
    # they are faster.

    # Comprensions are suitable for simple logic.


# write a program to generate table of 19 and store it in list.
# table_of_19 = []

# for i in range(1, 11):
#     table_of_19.append(i* 19)

# print(table_of_19) 

# List Comprehensions:-

# table_of_29 = [i * 29 for i in range(1, 11)]
# print(table_of_29)


# write a list coprehension which contains all even numbers
# E in between 1 to 20

# evens = [i for i in range(0, 21, 2)]
# print(evens)

# evens = [i for i in range(1, 21) if i%2 == 0 ]
# print(evens)

# str1 = "Gautemala Europe123%^&*"

# use str1 and create a list comprehension of consonens

# consonents = [i for i in str1 if i not in "aeiouAEIOU" and i.isalpha()]
# print(consonents)


# Write a list comprehension to get all the odd numbers 
# which are divisible by 3 and 7 in between of 1 and 100

# xyz = [num for num in range(1, 100) if num % 2 != 0 and num % 3 == 0 and num % 7 == 0]
# print(xyz)

# Write a program to get all numbers which are divisble by 
# 5 from str1

# str1 = "Film@#$750"

# result = [num for num in str1 if num.isnumeric() and int(num) % 5 == 0]
# print(result)

#-------------------

# tuple comprehension:-

# Write a tuple comprehension to print 1 to 10 numbers.

# tup1 = (i for i in range(1, 11))
# print(tup1)
# for i in tup1:
#     print(i, end=" ")

# Set Comprehension:

#------------------
# s1 = {num for num in range(20, 10, -2)}
# print(s1)


# dictionary Comprehension:

# Write a dict comprehension to get number 
# as a key and its square as a value  from 1 to 10

# dict1 = {1:1, 2:4, 3:9, 4:16}

# dict1 = {key: key**2 for key in range(1, 11)}
# print(dict1)
#-------------------------------------------
