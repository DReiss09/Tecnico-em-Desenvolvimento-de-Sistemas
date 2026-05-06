numinicio = int(input("Digite o número de inicio: "))
numfinal = int(input("Digite o número final: "))
soma = 0

for i in range(numinicio,numfinal + 1):
   if(i%2 == 0):
     soma = soma + i

print("A soma dos números entre" , numinicio," e ", numfinal," é:",soma)