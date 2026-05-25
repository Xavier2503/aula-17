numeros = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

soma_total = 0

# O primeiro loop entra em cada sublista
for lista_interna in numeros:
    # O segundo loop entra em cada número daquela sublista específica
    for numero in lista_interna:
        print(f"Número encontrado: {numero}")
        soma_total += numero  # Acumula o valor na variável soma_total

print("-" * 30)
print(f"A soma total de todos os números é: {soma_total}")