#Crie uma função chamada calcular_imc que receba o peso (em kg) e a altura (em metros)
#de uma pessoa e retorne o IMC (peso / altura²)

#A partir da função anterior, crie uma função classificar_imc que retorna a categoria do IMC:

# A baixo de 18.5: Abaixo do peso
# Entre 18.5 e 24.9: Peso normal
# Entre 25.0 e 29.9: Sobrepeso
# 30.0 ou mais: Obesidade

#Obs: Peça para o usuário informar os valores

def classificar_imc(imc):
  if imc < 18.5:
    return "Abaixo do peso"
  elif imc < 25.0: 
    return "Peso normal"
  elif imc < 30.0: 
    return "Sobrepeso"
  else: 
    return "Obesidade"

