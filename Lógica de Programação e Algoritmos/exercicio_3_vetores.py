numeros = []
soma = 0
media = 0

for i in range(4):
    num = int(input("Digite a nota: "))
    numeros.append(num)
    
for num in numeros:
    soma = soma + num
media = soma/4

if(media < 4):
    print("Reprovado: ", media)

elif(media >= 4 and media <= 7):
    print("Recuperação: ", media)

else:
     print("Aprovado!")
