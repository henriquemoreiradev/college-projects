''' 4.  Write a program that allows the user to ask you your height, favorite color, or favorite author and returns the result from the dictionary created in the previous challenge.    '''

henrique = {
    "Height":176,
    "Favorite color":"Azul",
    "Favorite author":"Jane Austen"
}

a = int(input("""What do you want to know?
Enter 0 for Height
Enter 1 for Favorite Color
Enter 2 for Favorite Author
: """))
if a == 0:
    print(henrique["Height"])
elif a == 1:
    print(henrique["Favorite color"])
elif a == 2:
    print(henrique["Favorite author"])
else:
    print("This is not an option")