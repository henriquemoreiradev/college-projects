'''
3.  Escreva um programa que exiba uma mensagem se uma variável for menor ou igual a 10, outra mensagem se a variável for maior do que 10, mas menor ou igual a 25, e ainda outra mensagem se a variável for maior do que 25.
'''

numero = float(input("Digite um número: "))

if numero > 25:
    print("O número digitado é maior do que 25")
elif 25 >= numero > 10:
    print("O número digitado fica entre 10 e 25")
else:
    print("O número digitado é menor ou igual a 10")