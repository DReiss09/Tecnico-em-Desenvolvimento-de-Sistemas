vetor = []
numero = 0

for i in range(8):
    num = int(input("Digite um número: "))
    vetor.append(num)


    num = int(input("Digite um número de busca:"))

for i in range(8):
    if(vetor[i] == num):
        print("Encontrou!")
