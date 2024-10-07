#5. Faça um programa que leia um número indeterminado de notas. Após esta entrada de dados, faça o seguinte: 
#   • Mostre a quantidade de notas que foram lidas.
#   • Exiba todas as notas na ordem em que foram informadas.
#   • Exiba todas as notas na ordem inversa à que foram informadas, uma abaixo do outra.
#   • Calcule e mostre a soma das notas.
#   • Calcule e mostre a média das notas.
#   • Calcule e mostre a quantidade de notas acima da média calculada

notas = []

contadorNotas = int(input("informe quantas notas serão listadas: "))

for i in range(contadorNotas):
    notas.append(float(input(f"Digite a {i+1}ª nota: ")))

print(f"Foram listadas {contadorNotas} notas")

print(f"As notas foram {notas}")

for i in reversed(notas):
    print(i)
  
somaNotas = sum(notas)
print(f"A soma das notas é {somaNotas}")

mediaNotas = sum(notas)/len(notas)
print(f"A média das notas é {mediaNotas}")

temp = 0
notasPositivas = 0

for i in range(contadorNotas):
    if notas[i] > mediaNotas:
        notasPositivas += 1

print(f"A quantidade de notas acima da média calculada é {notasPositivas}")