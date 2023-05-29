# Crie uma calculadora que faça operações de soma,subtração,divisão,mutiplicação e 
# exponenciação
# A função deve receber dois numeros e as operações que serão realizadas.

result = 0
def calculator(num1:float, sinal:str, num2:float):
    if sinal == "+":
        result = num1 + num2
        return result   
    elif sinal == "-":
        result = num1 - num2
        return result     
    elif sinal == "*":
        result = num1 * num2
        return result  
    elif sinal == "/":
        result = num1 / num2 
        return result 
    else:
        return ("Você não escolheu um operador válido")


num1 = float(input("Escolha o primeiro numero: "))
sinal = ""

while sinal != "=":
    sinal = input("Qual operação? ")
    num2 = float(input("Digite um outro número: "))
    calculadora = calculator(num1, sinal, num2)
    print(calculadora)
    num1 = calculadora

