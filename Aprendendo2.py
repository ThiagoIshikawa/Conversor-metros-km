# Conversor de unidades


def metros_para_km (metros):
        return metros / 1000
def km_para_metros (km):
        return km * 1000

while True:

    try:
    
        valor = float(input("Digite um valor em metros: "))

    except ValueError:
        print("Por favor, insira um número válido!")
        continue

    
    

    print("\nSelecione uma dessas opções: ")
    print("1. metros-km")
    print("2. km-metros")
    print("3. sair")
    
    operacao = input("Digite a operacao desejada: ")

    if operacao == "1":
        resultado = metros_para_km(valor)
        print("Resultado:", resultado, "km")
    elif operacao == "2":
        resultado = km_para_metros(valor)
        print("Resultado:", resultado, "metros")
    elif operacao == "3":
        print("saindo...")
        break
    else:
        print("Opção inválida")

    
