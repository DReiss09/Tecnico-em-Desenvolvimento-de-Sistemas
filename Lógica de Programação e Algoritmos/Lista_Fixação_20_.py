idades = []

for i in range(6):
    idades.append(input("Digite a idade: "))
    if(idades > 18):
        print("de maior!")
    elif(idades < 18):
        print("de menor")
    else:
        print("inválido")
