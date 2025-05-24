# Exemplo 3: Verificar Horário de Funcionamento

hora = int(input("Digite a hora atual (0 a 23): "))

if hora > 9 and hora < 18:
    print("Loja aberta.")
else:
    print("Loja fechada.")
    