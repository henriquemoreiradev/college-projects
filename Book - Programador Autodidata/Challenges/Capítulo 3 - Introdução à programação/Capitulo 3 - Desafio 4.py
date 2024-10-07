'''
4.  Crie um programa que divida duas variáveis e exiba o resto.
'''

numero = []

for i in range(2):
    numero.append(float(input(f"Digite o {i + 1}º número: ")))

resto = numero[0] % numero[1]
print(f"O resto é {resto}")