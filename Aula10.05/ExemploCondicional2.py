# Exemplo 2: Classificar Faixa Etária

idade = int(input("Qual sua idade? "))

if idade < 12:
    print("Criança")
elif idade < 18:
    print("Adolescente")
elif idade < 60:
    print("Adulto")
else:
    print("Idoso")
