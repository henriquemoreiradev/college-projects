#2. Ler uma lista de 10 números reais e mostre-os na ordem inversa.

numeros = []

for i in range(10):
  numeros.append(int(input(f"Digite o {i+1}º número: ")))

numeros.reverse()

for i in range(len(numeros)):
  print(numeros[i], end=" ")