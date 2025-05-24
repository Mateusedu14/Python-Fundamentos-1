#Crie um programa que simule um menu de opções com as seguintes ações:
#Dizer "Olá"
#Dizer a hora (use um print fixo, ex "São 14:30")
#Sair
#O programa deve repetir até o usuário escolher sair. 

opcoes = ["Dizer 'Olá'", "Dizer a hora", "Sair"]

while True:
    print("\nMenu de Opções:")
    for i in range(3):  # porque temos 3 opções fixas
        print(f"{i + 1} - {opcoes[i]}")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        print("Olá!")
    elif escolha == "2":
        print("São 14:30")
    elif escolha == "3":
        print("Saindo do programa. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")
         