#12 Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos deve obedecer à tabela acima.

notas = []

for i in range(2):
    notas.append(float(input(f"Digite a {i+1}ª nota: ")))

media = sum(notas)/len(notas)

if media >= 9:
    print("Conceito A")
elif media >= 7.5:
    print("Conceito B")
elif media >= 6:
    print("Conceito C")
elif media >= 4:
    print("Conceito D")
else:
    print("Conceito E")