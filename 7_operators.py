# Operators:

    # Arithmetic Operators:
        # Addition +
        # Substraction -
        # Multiplication *
        # True Division /
        # Floor Division //
        # Exponentiation (Power) **
        # Modulus (Mod)  %

# num1 = 5
# num2 = 3

# print(num1 + num2)
# print(num1 - num2)
# print(num1 * num2)
# print(num1 / num2)
# print(num1 // num2)
# print(num1 ** num2)
# print(num1 % num2)

# print(5**3*4-50+10/2)

# Comparision OPerators :

    # Greater than >
    # lesser than <
    # equal to ==
    # not equal to !=
    # greater than or equal to >=
    # lesser than or equal to <=

x = 34
y = 23
z = 55

# print( x > y > z)
# print(z < x > y)

# print(x != y)
# print(x == x)
# print(z <= y)
# print(z >= y)
#-----------------------------

# Identity Operators 
    # is
    # is not

# x = 5
# y = 5
# print( x is y)

# z = [1, 2, 3]
# w = z.copy()
# print(z)
# print(w)
# print(z is w)

# m = [1, 2, 3, [10, 20]]
# n = m.copy()
# print(m is not n)
# print(m[-1] is n[-1])
# print(id(m[-1]))
# print(id(n[-1]))

# print(m[0] is not n[0])
# import copy

# p = (12, 23, 34)
# q = copy.deepcopy(p)
# print(p is q)

#-------------------
# Membership Operators

    # in
    # not in

l1 = ["A", 12, 22, 3.3, True, 0]
# print(False in l1)
# print(1 in l1)
# print((24/2) in l1)
# print('a'.upper() not in l1)

# Logical OPerators:
    # and  # if any sub-statement is False then whole statement is False
    # or   # at least one sub-statement is True then whole statement is True
    # not

# x = 5
# y = 10
# z = 15

# print(x > y and y < z)
# False and True  
# print(x < y and x < z and y < z and z == z)

# print( x < y or y < z or z < x)

# print(x < z and y < z or x > y)

# print(not(x < y))

#-----------------------------

    # Bitwise Opearator:-


# print(ord("A"))
# print(ord("a"))
# print(ord("$"))

# print(bin(65))    #0b1000001


#-------------------

#   &   (and)
#   |   (or)
#   ^   (xor)

# print(51 & 20)   # 16
# print(bin(51))
# print(bin(20))

# print(int("10000", 2))

# print(51 | 20)   # 55
# print(bin(51))
# print(bin(20))

# print(int('110111', 2))  # 55


# print(51 ^ 20)   # 39
# print(bin(51))
# print(bin(20))

# print(int("100111", 2))


#----------------------------------

# Ternary Operator :

# Wrrite a program to display meaning of color provided by
# user.

# Red, Blue, Green

# color = input("Enter your favourate primary color: ")

# result = "Sacrifice" if color == "Red" else "Peace" if color == "Blue" else "Nature" if color == "Green" else "Invalid Color"

# print(result)

#--------------------------------

# Write a program to display grade on the basis of user provided 
# marks out of 100.
# 0 - 40  ==> Failed
# 40 - 60  ==> C
# 60 - 80  ==> B
# 80 - 100 ==> A

# marks = int(input("Enter your marks: "))

# result = "Fail" if marks < 40 else "C" if marks >= 40 and marks < 60 else "B" if marks >= 60 and marks < 80 else "A" if marks >= 80 and marks <= 100 else "Invalid Marks"
# print(result)
