#While

'''2 - O usuário digita vários números (um por vez). O programa só para quando
ele digitar 0. Ao final, mostre quantos números pares foram digitados.'''



contador_pares = 0


while True:
    numero = int(input("Digite um número (ou 0 para parar): "))
    
    
    if numero == 0:
        break
    
    elif numero % 2 == 0:
        contador_pares += 1


print(f"Você digitou {contador_pares} números pares.")

