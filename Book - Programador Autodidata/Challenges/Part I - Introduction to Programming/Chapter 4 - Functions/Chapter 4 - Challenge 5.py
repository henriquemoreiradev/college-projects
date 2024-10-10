''' 5.  Write a function that converts a string to a float and returns the result.
        Use exception handling to catch the exception that may occur.   '''

def funcao(a):
    return(float(a))

try:
    valor_a = input("Insira um número: ")
    
    print(funcao(valor_a))

except ValueError:
    print("isso não é um número.")