#Cadastre 4 visitantes de um museu. Para cada um, registre nome e idade. Guarde os
#dados em uma lista de tuplas. Depois mostre quem é o visitante mais velho e a média
#de idade.

visitantes = []

for i in range(4):
    nome = input(f"Digite o nome do visitante {i+1}: ")
    idade = int(input(f"Digite a idade do visitante {i+1}: "))
    visitantes.append((nome, idade))


mais_velho = visitantes[0]
for visitante in visitantes:
    if visitante[1] > mais_velho[1]:
        mais_velho = visitante


soma_idades = 0
for visitante in visitantes:
    soma_idades += visitante[1]
media_idade = soma_idades / len(visitantes)

print(f"\nVisitante mais velho: {mais_velho[0]} com {mais_velho[1]} anos")
print(f"Média das idades: {media_idade:.2f} anos")
