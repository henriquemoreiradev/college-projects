#10 Faça um programa que pede dois inteiro e armazene em duas variáveis. Em seguida, troque o valor das variáveis e exiba na tela

numero1 = int(input("Digite um numero: "))
numero2 = int(input("Digite outro numero: "))

numero3 = numero1
numero1 = numero2
numero2 = numero3

print(numero1)
print(numero2)