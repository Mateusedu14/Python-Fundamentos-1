#Peça ao usuário para cadastrar 3 produtos. Para cada produto, informe: nome e
#preço.
#Guarde essas informações em uma lista. Depois, mostre todos os produtods e seus
#preços e a média dos preços.

produtos = []  # lista para guardar os produtos

for i in range(3):
    nome = input(f"Digite o nome do produto {i+1}: ")
    preco = float(input(f"Digite o preço do produto {i+1}: "))
    produtos.append((nome, preco))  # guardando tupla (nome, preco)

print("\nProdutos cadastrados:")
soma_precos = 0
for produto in produtos:
    print(f"Produto: {produto[0]} - Preço: R$ {produto[1]:.2f}")
    soma_precos += produto[1]

media = soma_precos / len(produtos)
print(f"\nMédia dos preços: R$ {media:.2f}")
