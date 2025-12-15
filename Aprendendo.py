# calculadora simples

while True:
    try:
        numero1 = float(input("Digite o seu primeiro número: "))
        numero2 = float(input("Digite o seu segundo numero: "))
    except ValueError:
        print("Erro: Por favor, insira um número válido.")
        

    def somar (a, b):
        return a + b
    def subtrair (a, b):
        return a - b
    def multiplicar (a, b):
        return a * b
    def dividir (a, b):
        if b != 0:
            return a / b
        else:
            return "Erro: Não é possível dividir por 0"

    print("Selecione a operação: ")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    operacao = input("Digite o numero da operação desejada: ")



    if operacao == "1":
            resultado = somar(numero1, numero2)
    elif operacao == "2":
            resultado = subtrair(numero1, numero2)
    elif operacao == '3':
            resultado = multiplicar(numero1, numero2)
    elif operacao == '4':
            resultado = dividir(numero1, numero2)
    elif operacao == '5':
            print("Saindo...")
    break

