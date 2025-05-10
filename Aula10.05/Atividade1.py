#While

''' 1 - Crie um programa que escolha um número secreto de 1 a 10 (você define
esse número no código). O usuário deverá tentar adivinhar o número. O
programa deve continuar pedindo tentativas até o número correto ser
digitado. Ao final, mostre quantas tentativas foram feitas até o acerto.'''

numero_correto = 9  # Número secreto escolhido
tentativa = 0
contador = 0

# Mensagem inicial
print("Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número secreto entre 1 e 10.")

while tentativa != numero_correto:
    tentativa = int(input("Digite um número: "))
    contador += 1

print(f"Parabéns! Você acertou o número em {contador} tentativa(s).")
