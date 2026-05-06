numeros = []

for i in range(6):
    num = int(input("Digite um número: "))
    numeros.append(num)

print("Números pares:")
for num in numeros:
    if(num %2 == 0):
        print(num)




