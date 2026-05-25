import random

# O computador escolhe um número secreto
numero_secreto = random.randint(1, 100)
tentativas = 0
acertou = False

print("Tente adivinhar o número entre 1 e 100!")

while not acertou:
    palpite = int(input("Digite o seu palpite: "))
    tentativas += 1
    
    if palpite == numero_secreto:
        print(f"Parabéns! Você acertou em {tentativas} tentativas.")
        acertou = True
    elif palpite < numero_secreto:
        print("Mais alto... Tente novamente.")
    else:
        print("Mais baixo... Tente novamente.")