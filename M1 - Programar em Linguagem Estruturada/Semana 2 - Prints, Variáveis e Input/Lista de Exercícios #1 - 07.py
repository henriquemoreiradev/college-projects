#7. Realiza a leitura de 1 int e apresenta se ele é par ou ímpar.

numero = int(input("Digite um número: "))

if numero%2 == 0:
    print(f"O número {numero} é par")
else:
    print(f"O número {numero} é ímpar")