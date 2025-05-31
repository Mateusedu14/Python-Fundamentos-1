#Crie uma função mostrar_tabuada(numero) que receba um número inteiro e imprima a
#tabuada dele de 1 a 10. O programa deve permitir que o usuário digite vários números, até
#digitar 0 para encerrar.

def mostrar_tabuada(numero):
  """
  Imprime a tabuada de um número de 1 a 10.

  Args:
    numero (int): O número inteiro para o qual a tabuada será gerada.
  """
  print(f"--- Tabuada do {numero} ---")
  
  multiplicador = 1
  while multiplicador <= 10:
    resultado = numero * multiplicador
    print(f"{numero} x {multiplicador} = {resultado}")
    multiplicador = multiplicador + 1 



while True:
  
  entrada_usuario = input("Digite um número inteiro para ver a tabuada (ou 0 para sair): ")

  
  numero_digitado = int(entrada_usuario)

  
  if numero_digitado == 0:
    print("Programa encerrado. Até mais!")
    break 

  
  else:
    mostrar_tabuada(numero_digitado)
  print("\n") 