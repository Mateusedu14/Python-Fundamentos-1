frase = input("Digite uma frase (ou 'sair' para encerrar): ")
quantidade = 0

while frase != "sair":
    quantidade += len(frase.split())
    frase = input("Digite outra frase (ou 'sair' para encerrar): ")

    print("Você digitou", quantidade, "palavras.")
    