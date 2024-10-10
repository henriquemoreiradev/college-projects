'''Escreva uma função que converta uma string em um float e retorne o resultado. Use a
manipulação de exceções para capturar a exceção que pode ocorrer.'''

def funcao(a):
    return(float(a))

try:
    valor_a = input("Insira um número: ")
    
    print(funcao(valor_a))

except ValueError:
    print("isso não é um número.")