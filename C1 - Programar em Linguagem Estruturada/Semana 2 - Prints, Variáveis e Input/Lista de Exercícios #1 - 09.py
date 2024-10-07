#9. Faça um Programa que leia dois números inteiros e mostre o maior deles.

numeros = []

for i in range(2):
  numeros.append(int(input(f"Digite o {i+1}º numero: ")))

print(f"O maior numero é {max(numeros)}")