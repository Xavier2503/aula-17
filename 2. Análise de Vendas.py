meta = 10000
vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870],
]

print("Vendedores que bateram a meta:")
print("-" * 35)

# Como cada item da lista é outra lista com [nome, valor], podemos desempacotar direto no for:
for vendedor, valor in vendas:
    if valor >= meta:
        print(f"- {vendedor}: vendeu R$ {valor:,.2f}")