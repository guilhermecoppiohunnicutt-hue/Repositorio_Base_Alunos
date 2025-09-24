# Solicitamos dois números ao usuário sem informar o tipo de dado
num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")

try:
    num1 = int(num1)
    num2 = int(num2)

    print(f'Soma dos números = {num1 + num2}.')
except:
    print("Digite um numero correto.")