# Control Statements (LOOPS):-
    # TYpes of Loops:
        # While Loop:
            # It is manual
            # more control

        # For Loop:
            # It is automatic
            # less control

# write a program to print hello world.

# print('Hello World')

# Write a program to print hello world 1000000 times

# print("Hello Wolrd")
# print("Hello World")
# print("Hello Wolrd")
# print("Hello World")
# print("Hello Wolrd")

# Write a program to print "Hello World" 10 times using while loop.

# times = 0 # 10

# while times < 10:
#     print("Hello World", times)
#     times +=1

# -------------------------

# print 1 to 10 numbers using while loop.

# num = 1

# while num <= 10:
#     print(num)
#     num +=1
#---------------------------

# print all even numbers from 15 to 50

# num = 15

# while num <= 50:
#     if num % 2 == 0:
#         print(num)
#     num +=1


# ------------------------
# Write a program to ask user his / her name .
# using while loop find all vowels and print them

# name = input("Enter your name: ")  # shiva  5  [0, 1, 2, 3, 4]

# index = 0

# while index < len(name):
#     if name[index].lower() in 'aeiou':
#         print(name[index])
#     index +=1


#------------------------------

# Write a program to print fibonacci series 
# 0, 1, 1, 2, 3,5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 

# num_of_nums = int(input("How many numbers do you wanna generate of fibonacci: "))
# num1 = 0
# num2 = 1

# print(num1)
# print(num2)

# count = 2
# while count < num_of_nums:
#     new = num1 + num2
#     print(new)
#     num1 = num2
#     num2 = new
#     count += 1

#-----------------------------------

# Write a program to print all numbers which are divisible
# by 5 and 3 in between 100 and 50

# num = 100

# while num >= 50:
#     if num % 5 == 0 and num % 3 == 0:
#         print(num)
#     num -=1


#------------------------
# 153   ==> (1 ** 3) + (5** 3) + (3** 3)
        # ==> 1 + 125 + 27
        # 153

# 154  ==> (1 ** 3) + (5** 3) + (4** 3)
        # ==> 1 + 125 + 64
      # total =0
            # total += 1  = 1
            # total +=125 = 126
            # total += 64 = 190


# Write a program to print all 
# armstrong numbers from 100 to 10000

# num = 100   # convert to string
# while num <= 10000:
#     power = len(str(num))
#     total = 0
#     for digit in str(num):
#         total +=(int(digit) ** power) 
#     if total == num:
#         print(num)
#     else:
#         pass
#     num+=1

#================================

# For Loop:-

# Print Hello World 5 times using for loop
# range(5) ==> start = 0 , end = 5, step = 1

# for count in range(2,10, 2):   
#     print("Hello World", count)


# print table of 9 

# 9 * 1 = 9
# 9 * 2 = 18
# 9 * 3 = 27

# for num in range(1, 11):
#     print(f"9 * {num} = {num * 9}")

#---------------------------------

# Write a program to print all 
# non numeric charecters from string using for loop
# str1 = "aJg56q1%$#9"

# for char in str1:
#     if char.isnumeric():
#         pass
#     else:
#         print(char, end=" ")


#--------------------------

# Write a program  to print all numbers 
# which are divisible by 5 fromlist1 

list1 = ["A", 89, "G", 5, 10, 3, "&", True, 4.4, 25]

for x in list1:
    if isinstance(x, int):
        if x % 5 == 0:
            print(x)
        else:
            pass
    else:
        pass
    