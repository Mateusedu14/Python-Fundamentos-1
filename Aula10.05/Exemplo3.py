#1 - Sempre defina bem o que você quer fazer naquele bloco de código:

contador = 5

while contador > 0:
    print("Contando...", contador)
    contador = contador - 1 
    #agora vai parar

    #------------------------------------------------------#

#2 - Pode ser utilizado uma condição de parada (exemplo: input do usuário):

resposta = ""

while resposta != "sair":
    resposta = input("Digite 'sair' para encerrar: ")

  #------------------------------------------------------#

#3 - Podemos usar o break para forçar uma parada: 

while True: 
    comando = input("Digite um comando: ")
    if comando == "parar":
        break 