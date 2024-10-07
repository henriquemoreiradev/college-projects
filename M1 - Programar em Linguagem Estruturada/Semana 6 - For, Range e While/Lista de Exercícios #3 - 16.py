#16 Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

numeros = []

conjunto = int(input("Quantos números há no conjunto? "))

for i in range(conjunto):
  numeros.append(int(input(f"Digite o {i+1}º número: ")))


print(f"O menor valor é {min(numeros)}")
print(f"O maior valor é {max(numeros)}")
print(f"A soma dos valores é {sum(numeros)}")