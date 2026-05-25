produtos = ['iphone', 'galaxy', 'ipad', 'tv', 'máquina de café', 'kindle', 'geladeira', 'adega', 'notebook dell', 'notebook hp', 'notebook asus', 'microsoft surface', 'webcam', 'caixa de som', 'microfone', 'câmera canon']
vendas2019 = [558147,712350,573823,405252,718654,531580,973139,892292,422760,154753,887061,438508,237467,489705,328311,591120]
vendas2020 = [951642,244295,26964,787604,867660,78830,710331,646016,694913,539704,324831,667179,295633,725316,644622,994303]

print("Produtos com crescimento em 2020:")
print("-" * 60)

# O 'enumerate' nos dá o índice (i) e o nome do produto ao mesmo tempo
for i, produto in enumerate(produtos):
    venda_19 = vendas2019[i]
    venda_20 = vendas2020[i]
    
    # Verifica se vendeu mais em 2020 do que em 2019
    if venda_20 > venda_19:
        crescimento = (venda_20 / venda_19) - 1
        # :.1% formata o número automaticamente como porcentagem (ex: 0.705 -> 70.5%)
        print(f"Produto: {produto.title()}")
        print(f"  Vendas 2019: {venda_19} | Vendas 2020: {venda_20}")
        print(f"  Crescimento: {crescimento:.1%}\n")