#11 Altere o programa anterior para mostrar no final a soma dos números.

numero1 = int(input("Digite um numero inteiro: "))
numero2 = int(input("Digite outro numero inteiro: "))

numeros = []

for i in range(numero1+1,numero2):
  print(i)
  numeros.append(i)

print(f"A soma dos números é {sum(numeros)}")