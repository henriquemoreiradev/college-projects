'''
5.  Crie um programa que receba duas variáveis, as divida, e exiba o quociente.
'''

numero = []

for i in range(2):
    numero.append(float(input(f"Digite o {i + 1}º número: ")))

quociente = numero[0] / numero[1]

print(f"O quociente é {quociente}")