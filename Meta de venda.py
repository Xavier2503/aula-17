venda = [250, 330, 440, 540, 350, 250, 368, 40, 250, 30, 30]
vendedores = ['maria', 'mara', 'joão', 'silva', 'santos', 'mario', 'carlos', 'marly', 'xuxa', 'chica', 'zinha']

meta = 50
i = 0

# O loop roda enquanto 'i' for menor que o tamanho da lista de vendas
while i < len(venda):
    if venda[i] >= meta:
        print(f"Vendedor(a) {vendedores[i]} bateu a meta! Vendeu: {venda[i]}")
    i += 1