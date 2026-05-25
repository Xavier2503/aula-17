soma = 0
numero = 1

while soma <= 20:
    soma += numero
    print(f"Somando {numero}... Soma atual: {soma}")
    numero += 1

print(f"\nA soma final ultrapassou 20! Total: {soma}")