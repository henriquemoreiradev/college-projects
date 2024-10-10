''' 3.  Write a program that displays one message if a variable is less than or equal to 10, another message if the variable is greater than 10 but less than or equal to 25, and yet another message if the variable is greater than 25.   '''

x = 11
if x <= 10:
    print("é menor ou igual a 10")
elif x > 10 and x <= 25:
    print("é maior que 10, mas menor ou igual a 25")
else:
    print("é maior do que 25")