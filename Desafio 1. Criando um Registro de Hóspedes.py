qtd_pessoas = int(input("Quantas pessoas vão ficar no quarto (1 a 4)? "))
quarto = []

# O loop 'for' vai rodar o número de vezes que o usuário digitou
for i in range(qtd_pessoas):
    print(f"\n--- Cadastro da {i+1}ª pessoa ---")
    nome = input("Digite o nome: ")
    cpf = input("Digite o CPF: ")
    
    # Adiciona a sublista [nome, cpf] dentro da lista 'quarto'
    quarto.append([nome, f"cpf:{cpf}"])

print("\nCadastro finalizado com sucesso!")
print("Quarto:", quarto)
