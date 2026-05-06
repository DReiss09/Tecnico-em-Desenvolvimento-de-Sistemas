valorDaCompra = float(input("Digite o valor da compra: "))
cupomDesconto = input("Possui cupom de desconto? ")

if(valorDaCompra >= 200 or cupomDesconto == "Sim"):
    print("Voce ganhou um desconto de 15%!")
else:
    print("Voce não tem direito a desconto no momento!")