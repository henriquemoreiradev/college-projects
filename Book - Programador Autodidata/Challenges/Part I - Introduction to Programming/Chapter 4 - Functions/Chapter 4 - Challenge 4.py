''' 4.  Write a program with two functions. 
        The first function should take an integer as a parameter and return the result of the integer divided by 2.
        The second function should take an integer as a parameter and return the result of the integer multiplied by 4.
        Call the first function, save the result as a variable, and pass it as a parameter to the second function.  '''

#   construir a primeira função
valor_a = 8

def funcao_a(a):
    return int(a/2)

print(funcao_a(valor_a))

#   construir a segunda função
valor_b = funcao_a(valor_a)

def funcao_b(b):
    return int(b*4)

print(funcao_b(valor_b))