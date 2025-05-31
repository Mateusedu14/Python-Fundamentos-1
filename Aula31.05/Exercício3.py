#Crie uma função celsius_para_fahrenheit que receba uma temperatura em Celsius e retorne
#o equivalente em Fahrenheit. Peça para o usuário informar um valor.

def celsius_para_fahrenheit(celsius):
  
  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit


temperatura_celsius_str = input("Digite a temperatura em Celsius: ")


temperatura_celsius = float(temperatura_celsius_str)


temperatura_fahrenheit = celsius_para_fahrenheit(temperatura_celsius)


print(f"A temperatura de {temperatura_celsius}°C equivale a {temperatura_fahrenheit}°F.")