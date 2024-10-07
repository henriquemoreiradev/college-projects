#3. Ler uma lista com 4 notas, em seguida o programa deve exibir as notas e a média.

notas = []

for i in range(4):
  notas.append(float(input(f"Digite a {i+1}ª nota: ")))

media = sum(notas)/len(notas)

print(f"As {len(notas)} notas foram: {notas} e a média é: {media}")