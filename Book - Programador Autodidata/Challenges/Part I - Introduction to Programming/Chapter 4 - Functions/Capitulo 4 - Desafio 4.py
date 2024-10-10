'''Escreva um programa com duas funções. A primeira função deve receber um inteiro como parâmetro
e retornar o resultado do inteiro dividido por 2. A segunda função deve receber um inteiro como
parâmetro e retornar o resultado do inteiro multiplicado por 4. Chame a primeira função, salve o
resultado como uma variável e passe-a como parâmetro para a segunda função.'''

#construir a primeira função
valor_a = 8

def funcao_a(a):
    return int(a/2)

print(funcao_a(valor_a))

#construir a segunda função
valor_b = funcao_a(valor_a)

def funcao_b(b):
    return int(b*4)

print(funcao_b(valor_b))