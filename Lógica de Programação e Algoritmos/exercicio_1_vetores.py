numeros = []

for i in range(10):
    num = int(input("Digite um número: "))
    numeros.append(num)

cont_pares = 0

for numero in numeros:
    if(num%2 == 0):
        cont_pares = cont_pares + 1
print("Número pares: ", cont_pares)

