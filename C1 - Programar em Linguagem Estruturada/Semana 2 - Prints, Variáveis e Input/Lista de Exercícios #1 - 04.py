#4. Realiza a leitura de 3 floats e imprime a média aritmética.

media = []

for i in range(3):
    media.append(float(input(f"Digite o {i+1}º número: ")))

print(f"A média de {media[0]}, {media[1]} e {media[2]} é {sum(media)/len(media)}")