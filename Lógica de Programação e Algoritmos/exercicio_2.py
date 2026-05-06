pi = 3.14
raio = int(input("Digite o raio: "))
altura = int(input("Digite a altura: "))

area = 2*pi*raio*(raio+altura)
volume = pi*raio*raio*altura

print("Volume: ", volume)
print("Área: ", area)