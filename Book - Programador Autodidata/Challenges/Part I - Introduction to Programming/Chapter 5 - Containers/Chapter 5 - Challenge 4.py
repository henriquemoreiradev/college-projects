''' 4.  Write a program that allows the user to ask you your height, favorite color, or favorite author and returns the result from the dictionary created in the previous challenge.    '''

henrique = {
            "Altura":176,
            "Cor favorita":"Azul",
            "Autor favorito":"Jane Austen"
}

a = int(input("""O que você quer saber?
          Digite 0 para Altura
          Digite 1 para Cor favorita
          Digite 2 para Autor favorito
          """))
if a == 0:
    print(henrique["Altura"])
elif a == 1:
    print(henrique["Cor favorita"])
elif a == 2:
    print(henrique["Autor favorito"])
else:
    print("Essa não é uma opção")