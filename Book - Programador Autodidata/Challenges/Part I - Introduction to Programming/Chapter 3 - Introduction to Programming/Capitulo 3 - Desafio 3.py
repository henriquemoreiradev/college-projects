'''Escreva um programa que exiba uma mensagem se uma variável for menor ou igual a 10, outra
mensagem se a variável for maior do que 10, mas menor ou igual a 25, e ainda outra mensagem se a
variável for maior do que 25.'''

x = 11
if x <= 10:
    print("é menor ou igual a 10")
elif x > 10 and x <= 25:
    print("é maior que 10, mas menor ou igual a 25")
else:
    print("é maior do que 25")