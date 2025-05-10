#For

''' 3 - Peça um número ao usuário e imprima a tabuada dele de 10 até 1 (ordem
decrescente).'''


numero = int(input("Digite um número: "))

for i in range(10, 0, -1):
    print(numero, "x", i, "=", numero * i)

