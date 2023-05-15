#dois numeros, um sinal, e resolver a operação do sinal
num1=float(input("Digite o primeiro numero"))
num2=float(input("Digite o segundo numero"))
sinal=input("Digite o sinal desejado para a operação")

if sinal == "+":
    print(num1 + num2)

elif sinal == "-":
    print(num1-num2)

elif sinal == "*":
    print(num1*num2)

elif sinal == "/":
    print(num1/num2)