#Crie um programa que:

#Permita ao usuário cadastrar 3 filmes que ele assistiu recentemente. Para cada 
#filme, peça:

#O título do filme
#A nota que o usuário dá de 0 a 10

#Guarde essa informações em uma lista aninhada (cada filme é uma sublista com título
# e nota). Ao final, exiba todos os filmes com sua respectiva nota, e destaque quais
#receberam nota maior ou igual a 8 como "Recomendado!".


filmes = []

for i in range(3):
    titulo = input(f"Digite o título do filme {i+1}: ")
    while True:
        try:
            nota = float(input(f"Digite a nota do filme {i+1} (0 a 10): "))
            if 0 <= nota <= 10:
                break
            else:
                print("Por favor, digite uma nota entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

    filmes.append([titulo, nota])

print("\nFilmes cadastrados:")
for filme in filmes:
    titulo, nota = filme
    if nota >= 8:
        print(f"{titulo} - Nota: {nota} - Recomendado!")
    else:
        print(f"{titulo} - Nota: {nota}")
