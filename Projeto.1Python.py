
#Projeto 01 - Calculadora Interativa
#Criar uma calculadora que realiza as 4 operações básicas (+, -, *, /) e aceita
#múltiplos cálculos em sequência.
#Habilidades trabalhadas:
#• Manipulação de entrada de usuário (input( ))
#• Uso de funções para organizar o código
#• Laços (while) e condicionais (if)

def soma():
    num1 = float(input("Primeiro numero: "))
    num2 = float(input("Segundo numero: "))
    print("Soma: ", num1+num2)

def subtração():
    num1 = float(input("Primeiro numero: "))
    num2 = float(input("Segundo numero: "))
    print("subtração: ", num1-num2)

def multiplicação():
    num1 = float(input("Primeiro numero: "))
    num2 = float(input("Segundo numero: "))
    print("multiplicação: ", num1*num2)


def divisão():
    num1 = float(input("Primeiro numero: "))
    num2 = float(input("Segundo numero: "))
    print("divisão: ", num1/num2)

opcao = 1

while opcao:
    print("0. sair")
    print("1. somar")
    print("2. subtrair")
    print("3. multiplicação")
    print("4. divisão")

    opcao = int(input("opção: "))

    if(opcao==1):
        soma()
    if(opcao==2):
        subtração()
    if(opcao==3):
        multiplicação()
    if(opcao==4):
        divisão()



            

    





