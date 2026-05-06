numero = int(input("Digite o número:"))

if(numero % 5 == 0):
    print("Esse número é múltiplo de 5✅")
elif(numero % 5 != 0):
    print("Esse número não é múltiplo de 5❌")
else:
    print("Inválido")