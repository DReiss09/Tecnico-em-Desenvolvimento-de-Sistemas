idade = int(input("Digite sua idade: "))
carteira = input("Voce tem CNH? ")

if(idade >= 18 and carteira == "Sim"):
    print("Voce pode dirigir! 🚗👌")
elif(idade >= 18 and carteira == "Não"):
    print("Voce não pode dirigir! 🚗❌")
else:
    print("ERRO!")
