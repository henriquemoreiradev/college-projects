#15 Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
#   • Ex.: 5!=5.4.3.2.1=120

numero = int(input("Digite um numero inteiro: "))

fatorial = []

for i in range(numero):
  fatorial.append(i+1)

fatorial.reverse()

resultado = 1

for i in range(numero):
  resultado = resultado*fatorial[i]

print(resultado)