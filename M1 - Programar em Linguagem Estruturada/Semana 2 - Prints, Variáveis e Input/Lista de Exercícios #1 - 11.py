#11 As Organizações Hamurabi Medeiros resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes.
#   • Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#     • salários até R$ 280,00 (incluindo) : aumento de 20%
#     • salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#     • salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#     • salários de R$ 1500,00 em diante : aumento de 5%
#   • Após o aumento ser realizado, informe na tela:
#     • o salário antes do reajuste;
#     • o percentual de aumento aplicado;
#     • o valor do aumento;
#     • o novo salário, após o aumento.

salario = float(input("Digite o salario: R$"))

print(f"o salário antes do reajuste é R${salario}")

if salario >= 1500:
    salarioReajustado = salario*1.05
    print("O percentual de aumento aplicado foi de 5%")
elif salario >= 700:
    salarioReajustado = salario*1.1
    print("O percentual de aumento aplicado foi de 10%")
elif salario > 280:
    salarioReajustado = salario*1.15
    print("O percentual de aumento aplicado foi de 15%")
else:
    salarioReajustado = salario*1.2
    print("O percentual de aumento aplicado foi de 20%")

print(f"O valor do aumento foi de R${round(salarioReajustado-salario,2)}")
print(f"O novo salário, após o aumento é R${round(salarioReajustado,2)}")