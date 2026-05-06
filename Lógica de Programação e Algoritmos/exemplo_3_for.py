num = int(input("Digite um número: "))
fatorial = 1

for i in range(num,0,-1):
    fatorial = fatorial * i
print(num,"! = ",fatorial)
    
