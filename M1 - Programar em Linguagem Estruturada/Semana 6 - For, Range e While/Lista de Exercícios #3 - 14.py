#14 Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

numeros = []

for i in range(10):
  numeros.append(int(input(f"Digite o {i+1}º número inteiro: ")))

impares = 0
pares = 0

for i in range(len(numeros)):
  if numeros[i]%2 == 0:
    pares += 1
  else:
    impares += 1

print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")