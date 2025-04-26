#Peça três números ao usuário e diga qual é o maior deles.

num1 = float(input("Digite o primeiro número:"))
num2 = float(input("Digite o segundo número:"))
num3 = float(input("Digite o terceiro número:"))

if num1 > num2 and num1 > num3:
    print("O Primeiro número é o maior")
elif num2 > num1 and num2 > num3:
    print("O Segundo número é o maior")
else: 
    print("O Terceiro número é o maior")