#Peça ao usuário uma nota de 0 a 10.

#Mostre se ele está:
#Aprovado (nota >=7)
#Recuperação (nota entre 5 e 6.9)
#Reprovado (nota < 5)

nota = float(input("Informe sua nota: "))

if nota < 5:
    print("Você está reprovado")
elif nota >= 5 and nota <= 6.9:
    print("Você está de recuperação")
else:
    print("Você está aprovado")
