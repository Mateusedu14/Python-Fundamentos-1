# Peça ao usuário um número inteiro. Informe se ele é multiplo de 3, 5, ambos ou nenhum.

numero = int(input("Digite um número: "))

if numero % 3 == 0 and numero % 5 == 0:
    print(f"{numero} é multiplo de 3 e 5")
elif numero % 3 == 0:
    print(f"{numero} é multiplo de 3")
elif numero % 5 == 0:
    print(f"{numero} é multiplo de 5")
else:
    print((f"{numero} não é multiplo nem de 3 e nem de 5"))
