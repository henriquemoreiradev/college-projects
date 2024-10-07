#4. Ler um vetor com 20 idades e exibir a maior e menor.

idades = []

for i in range(20):
    idades.append(int(input(f"Digite a {i+1}ª idade: ")))

maiorIdade = max(idades)
menorIdade = min(idades)

print(f"A maior idade é: {maiorIdade}")
print(f"A menor idade é: {menorIdade}")