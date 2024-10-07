'''
6.  Escreva um programa com uma variável age que receba um inteiro e exiba strings diferentes dependendo de que inteiro age receber.
'''

age = int(input("Diite sua idade: "))

if 60 <= age < 65:
    print("Você vai se aposentar em breve.")
elif age < 60:
    print("Você tem muito tempo até poder se aposentar!")