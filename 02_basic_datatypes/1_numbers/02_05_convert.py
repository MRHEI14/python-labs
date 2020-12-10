'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''
#1
x = 2
type(x)
print(type(x))

x_float = float(x)
print(type(x_float))

#2
x = 2.0
type(x)
print(type(x))

x_int = int(x)
print(type(x_int))

#3
division = 5 / 2.
print(division)

#4
x = int(input("input amount x: "))
y = int(input("input amount y: "))
multip = x * y
print(multip, "is the total amount")






