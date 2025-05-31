def contar_caracteres(texto):
    return len(texto)

texto = input("Digite uma palavra: ")
print(f'A palavra que você digitou tem {contar_caracteres(texto)} letras')
