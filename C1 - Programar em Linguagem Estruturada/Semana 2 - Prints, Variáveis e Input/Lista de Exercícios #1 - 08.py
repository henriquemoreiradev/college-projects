#8. Faça um programa que pede duas notas de um aluno. Em seguida ele deve calcular a média do aluno e dar o seguinte resultado:
#   • A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#   • A mensagem "Reprovado", se a média for menor do que sete;
#   • A mensagem "Aprovado com Distinção", se a média for igual a dez.

notas = []

for i in range(2):
    notas.append(float(input(f"Digite a {i+1}ª nota: ")))

media = sum(notas)/len(notas)

if media == 10:
    print("Aprovado com Distinção")
elif media >= 7 and media < 10:
    print("Aprovado")
elif media < 7 and media >= 0:
    print("Reprovado")
else:
    print("Média inválida")