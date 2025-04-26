#AT3 - Desenvolva um programa que receba o peso (em kg) e a altura (em metros) de uma pessoa, calcule o IMC (Índica de Massa Corporal) e mostre o resultado.
# Formula: IMC = peso / (altura²)


print("Vamos calcular o seu IMC")

peso = float(input("Digite seu peso: "))
altura = float(input("Digite a sua altura: "))

IMC = peso / (altura**2)

print(f"O seu IMC é: {IMC}")

