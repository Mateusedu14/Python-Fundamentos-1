# Peça o nome de usuário e a senha. Só permita o acesso se o usuário for "admin" e a senha for "1234"

user = input("Informe seu usuário: ")
senha = input("Informe sua senha: ")

if user == "admin"and senha == "1234":
    print("Acesso Liberado")
else:
    print("Acesso Negado")