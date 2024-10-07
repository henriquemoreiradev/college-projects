#8 Faça um programa que leia 5 números e informe a soma e a média dos números.

numeros = []

for i in range(5):
  numeros.append(int(input(f"Informe o {i+1}º número: ")))

print(f"a soma é {sum(numeros)}")
print(f"a média é {sum(numeros)/len(numeros)}")