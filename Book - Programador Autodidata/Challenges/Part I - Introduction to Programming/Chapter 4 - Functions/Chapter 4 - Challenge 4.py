''' 4.  Write a program with two functions. 
        The first function should take an integer as a parameter and return the result of the integer divided by 2.
        The second function should take an integer as a parameter and return the result of the integer multiplied by 4.
        Call the first function, save the result as a variable, and pass it as a parameter to the second function.  '''

def divide(number):
    return number / 2

def multiply(number):
    return number * 4

number_one = divide(8)
number_two = multiply(number_one)

print(number_two)