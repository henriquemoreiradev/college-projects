#3 Faça um programa que leia e valide as seguintes informações:
#   • Nome: maior que 3 caracteres;
#   • Idade: entre 0 e 150;
#   • Salário: maior que zero;
#   • Sexo: 'f' ou 'm';
#   • Estado Civil: 's', 'c', 'v', 'd'

while True:
  nome = input("Digite o nome: ")
  if len(nome) > 3:
    break
  else:
    print("O nome deve possuir mais de 3 caracteres.")

while True:
  idade = int(input("Digite a idade em anos: "))
  if 0 <= idade <= 150:
    break
  else:
    print("A idade deve estar entre 0 e 150 anos.")

while True:
  salario = float(input("Digite o valor do salário: "))
  if salario > 0:
    break
  else:
    print("O salário deve ser maior que zero.")

while True:
  sexo = input("Digite o sexo ('f' para feminino e 'm' para masculino): ")
  if sexo == "f" or sexo == "m":
    break
  else:
    print("Sexo inválido.")

while True:
  estadoCivil = input("Digite Estado Civil ('s', 'c', 'v' ou 'd'): ")
  if estadoCivil == "s" or estadoCivil == "c" or estadoCivil == "v" or estadoCivil == "d":
    break
  else:
    print("Estado civil inválido!")
    print("Deve ser 's' para solteiro, 'c' para casado, 'v' para viúvo e 'd' para divorciado")