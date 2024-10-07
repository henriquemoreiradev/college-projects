#10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

celsius = float(input("Digite a temperatura em graus Celsius: "))

fahrenheit = 1.8*celsius+32

print(f"A temperatura em graus Fahrenheit é {round(fahrenheit,2)}ºF")