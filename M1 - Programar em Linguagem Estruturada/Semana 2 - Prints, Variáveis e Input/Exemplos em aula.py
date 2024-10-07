# Exemplo 1

preco = input("diz o preço: ")
print("R$"+preco)

# Exemplo 2

numero1 = 100
numero2 = 80.1
soma = numero1 + numero2
print("A soma é",soma)

# Exemplo 3

numero1 = input("diz ai: ")
numero2 = input("diz ai: ")
soma = numero1 + numero2
print("A soma é",soma)

# Exemplo 4

nome = input("Diz o seu nome: ")
sobrenome = input("Diz o seu sobrenome: ")
nomeCompleto = nome + " " + sobrenome
print("O nome completo é", nomeCompleto)

# Exemplo 5

idadeStr = input("Qual a sua idade? ") #"38"
idade = int(idadeStr) #38
print("Proximo ano vc vai ter",idade+1)


# Exemplo 6

idade = int(  input("Qual a sua idade? ")  )
print("Proximo ano vc vai ter",idade+1)


# Exemplo 7

nota1 = float(input("Qual a sua nota: "))
nota2 = float(input("Qual a sua nota: "))
nota3 = float(input("Qual a sua nota: "))
media = (nota1 + nota2 + nota3) / 3
print("Sua média é",media)


# Exemplo 8 

nota1 = float(input("Qual a sua nota: "))
nota2 = float(input("Qual a sua nota: "))
nota3 = float(input("Qual a sua nota: "))
media = (nota1 + nota2 + nota3) / 3
mediaArredondada = round(media,2)
print("Sua média é",mediaArredondada)


# Exemplo 9

nota1 = float(input("Qual a sua nota: "))
nota2 = float(input("Qual a sua nota: "))
nota3 = float(input("Qual a sua nota: "))
media = (nota1 + nota2 + nota3) / 3
media = round(media,2)
print("Sua média é",media)