#10 Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles

numero1 = int(input("Digite um numero inteiro: "))
numero2 = int(input("Digite outro numero inteiro: "))

for i in range(numero1+1,numero2):
  print(i)