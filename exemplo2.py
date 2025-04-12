#exemplo 1: Entrada de dados do usuário



nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

print("Olá, ", nome + "! Você tem", idade, "anos.")
print(f'Olá {nome}! Você tem {idade} anos.')



#exemplo 2: Entrada de número e cálculo

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o Segundo número: "))

num3 = float(input("Digite o primeiro número: "))
num4 = float(input("Digite o Segundo número: "))

soma = num1 + num2
soma2 = num3 + num4

print(soma)
print(soma2)

#exemplo 3: Usando variáveis para fazer uma média

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a primeira nota: "))

media = (nota1 + nota2) / 2

print("A média é: ", media)