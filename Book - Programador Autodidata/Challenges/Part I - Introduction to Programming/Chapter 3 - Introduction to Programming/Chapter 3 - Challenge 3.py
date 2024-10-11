''' 3.  Write a program that displays one message if a variable is less than or equal to 10, another message if the variable is greater than 10 but less than or equal to 25, and yet another message if the variable is greater than 25.   '''

number = 11
if number <= 10:
    print("is less than or equal to 10")
elif number > 10 and number <= 25:
    print("is greater than 10 but less than or equal to 25")
else:
    print("is greater than 25")