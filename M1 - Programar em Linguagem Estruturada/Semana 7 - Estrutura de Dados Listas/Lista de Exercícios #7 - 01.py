#1. Ler uma lista de 5 números inteiros e  mostre cada número juntamente com a sua posição na lista.

numeros = []

for i in range(5):
    numeros.append(int(input(f"Digite o {i+1}º número inteiro: ")))

for i in range(len(numeros)):
    print(f"O número {numeros[i]} está na posição {i} da lista")