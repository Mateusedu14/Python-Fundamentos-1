def calculadora(a, b, resultado):
    if resultado == '+':
        return a + b
    elif resultado == '-':
        return a - b
    elif resultado == '*':
        return a * b
    elif resultado == '/':
        if b == 0 and a == 0:
            return "Erro: divisão por zero"
        return a / b
    else:
        return "Operação inválida :("

a = float(input("Digite o primeiro número da operação: "))    
b = float(input("Digite o primeiro número da operação: "))    
operacao = input("Digite qual a operação (soma, subtração, multiplicação ou divisão):")
print(calculadora(a, b, operacao))