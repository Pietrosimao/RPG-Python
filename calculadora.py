# FUNCOES DAS OPERAÇOES
def funcao_adicao(a,b):
    return a + b

def funcao_subtracao(a,b):
    return a - b

def funcao_multiplicacao(a,b):
    return a*b

def funcao_divisao(a,b):
    return a/b

#INTERFACE DO TERMINAL
print("Bem vindo a calculadora do Pietro")

operaçao = input("Qual operaçao deseja fazer?")

a = float(input("Qual o primeiro numero?"))
b = float(input("Qual o segundo numero?"))

if operaçao == "+":
    print("O resultado é:",(funcao_adicao(a,b)))

elif operaçao == "-":
    print("O resultado é:",(funcao_subtracao(a,b)))

elif operaçao == "x":
    print("O resultado é:",(funcao_multiplicacao(a,b)))

elif operaçao == "/":
    print("O resultado é:",(funcao_divisao(a,b)))



