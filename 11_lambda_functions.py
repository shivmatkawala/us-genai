# LAMBDA:-

    # a nameless function.
    # lambda is a conscise form of function
    # it is recommended to use lambda functions as they increase 
    # readibility, maintainability.
    # use lambda for easy and simple logic.
    # reusibilty of code will increase

# lambda arguments: expression 

# Write a lambda function to square the number.

# square = lambda num: num**2
# print(square(5))


# Write a lambda function to capitalize an alphabetic charecter.

# capital = lambda char: str(char).upper()
# print(capital("apple"))

# Write a lambda function to double the number.

# double = lambda num: 2* num
# print(double(5))
# print(double(12))
# print(double(19))

#-----------------------------

# Write a lmabda function which will reverse the string.

# reverse = lambda string: string[::-1]
# print(reverse("apple"))

# write a lambda function to check if number is divisble by 7

# divisible_by_7 = lambda num: num%7 == 0
# print(divisible_by_7(91))
# print(divisible_by_7(20))

#-----------------------------------

# write a lambda function which returns binary of charecter
# binary = lambda char: bin(ord(char))
# print(binary("A"))

#------------------- map, filter, reduce -------------------

# map() ==> it applies a function to every item in an iteracble /collection

# list1 = [2, 5, 9, 1, 3, 6]
# result = list(map(lambda num: num*2, list1))
# print(result)

# for i in list1:
#     print(double(i))

# dd = [double(num) for num in list1 ]
# print(dd)

# count = 0
# while count < len(list1):
#     print(double(list1[count]))
#     count +=1

#------------------------------------
# using map function get the list of consonensts from str1 string.
# str1 = "Gautemala"
# result = list(map(lambda char: char if char.lower() not in "aeiou" else None, str1))
# print(result)

#------------------------------------

# number = 123456

# print(int(str(number)[1]) ** 3)
# result = tuple(map(lambda num: int(num) **3, str(number)))
# print(result)

#---------------------------

# filter()  :-  keeps only items where the condition is true

# str1 = "AppLeSj"
# using filter function get a list of all capital letters

# result = list(filter(lambda char: char == char.upper(), str1))
# print(result)

# lower = list(filter(lambda char: char == char.lower(), str1))
# print(lower)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 
# result = list(filter(lambda num: num% 2 != 0, numbers))
# print(result)

# result = list(filter(lambda num: num% 2== 0, numbers))
# print(result)

str1 = "ap#12*.k"
# get me all special charecters

# result = list(filter(lambda char: not(char.isalnum()), str1))
# print(result)

# list1 = [89, 23, 55, 100, 78, 20, 11, 50]

# get me all those numbers which are less than 50

# result = list(filter(lambda num: num < 50, list1))
# print(result)


#------------------------------
# reduce() repeatedly applies a function to combine 
# values into  one result 

from functools import reduce

# reduce(function, iterable) 

list1 = [5, 2, 9, 8, 1, 14, 7]

# get the sum of list1

# result = reduce(lambda num1, num2: num1+num2, list1)
# print(result)

# result = reduce(lambda num1, num2: num1 * num2, list1)
# print(result)

# maximun number from list2

list2 = [23, 45, 1, 78, 99, 23, 0, 6]

# result = reduce(lambda num1, num2: num1 if num1 > num2 else num2, list2)
# print(result)

# result = reduce(lambda num1, num2: num1 if num1 < num2 else num2, list2)
# print(result)

