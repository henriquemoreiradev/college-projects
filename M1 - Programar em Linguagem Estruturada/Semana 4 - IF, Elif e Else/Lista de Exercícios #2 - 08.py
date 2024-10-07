#8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#   • Calcule e mostre o total do seu salário no referido mês.

salarioHora = float(input("Digite quanto você recebe por hora: "))
horasMes = float(input("Digite quantos horas por mês você trabalha: "))

salarioMes = salarioHora*horasMes

print(f"O salário do mês é R${salarioMes}")