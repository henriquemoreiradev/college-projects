#7 Faça um programa que leia 5 números e informe o maior número.

numeros = []

for i in range(5):
  numeros.append(int(input(f"Informe o {i+1}º número: ")))

print(f"O maior número é {max(numeros)}")