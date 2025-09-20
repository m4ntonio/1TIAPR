import random

numero_secreto = random.randint(1, 10)
tentativas = 3

while tentativas > 0:
    palpite = int(input("Adivinhe o número entre 1 e 10: "))
    if palpite == numero_secreto:
        print("Parabéns! Você acertou!")
        break
    else:
        tentativas -= 1
        if tentativas > 0:
            print(f"Errado! Você tem {tentativas} tentativa(s) restante(s).")
        else:
            print(f"Suas tentativas acabaram. O número era {numero_secreto}.")