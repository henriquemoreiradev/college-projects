''' 5.  Write a function that converts a string to a float and returns the result.
        Use exception handling to catch the exception that may occur.   '''

def function_float(number):
    return(float(number))

try:
    number = input("Enter a number: ")
    
    print(function_float(number))

except ValueError:
    print("This is not a number.")