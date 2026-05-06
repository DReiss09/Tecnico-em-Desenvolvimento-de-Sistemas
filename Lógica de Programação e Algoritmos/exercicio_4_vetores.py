numeros = []
invertido = [0,0,0,0,0]

for i in range(5):
    num = int(input("Digite um número: "))
    numeros.append(num)
    
for i in range(5):
   invertido[i] = num[4-i]

print(invertido)