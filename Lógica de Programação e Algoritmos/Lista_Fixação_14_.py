qtd_positivos = 0
qtd_negativos = 0

for i in range(10):
    numero = int(input("Digite os números: "))
    if(numero > 0):
        qtd_positivos = qtd_negativos +1
    elif(numero < 0):
        qtd_negativos = qtd_positivos +1
print("A quantidade de positivos:", qtd_positivos)
print("A quantidade de negativos:", qtd_negativos)


