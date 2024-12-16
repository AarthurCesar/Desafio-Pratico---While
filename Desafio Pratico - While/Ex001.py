# 1 - Soma de Números Pares:
# Crie um programa que use um laço while para somar
# todos os números pares de 1 a 100 e exiba o resultado.

numero = 1

soma = 0

while numero <= 100:
    if numero % 2 == 0:
        soma += numero
    numero += 1
print (f"Soma de todos os números é {soma}")

