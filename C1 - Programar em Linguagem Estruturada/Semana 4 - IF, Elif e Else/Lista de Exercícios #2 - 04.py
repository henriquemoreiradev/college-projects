#4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.

notas = []

for i in range(4):
  notas.append(float(input(f"Digite a {i+1}ª nota: ")))

media = sum(notas)/len(notas)

print(f"A media é {media}")