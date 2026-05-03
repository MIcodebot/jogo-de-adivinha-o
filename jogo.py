import random

def jogo_adivinhacao():
    """Jogo de adivinhacao de numero."""
    print("=" * 40)
    print("  🎮 JOGO DE ADIVINHACAO  ")
    print("=" * 40)
    print("Estou pensando em um numero entre 1 e 100.")
    print("Tente adivinhar!\n")

    numero_secreto = random.randint(1, 100)
    tentativas = 0
    acertou = False

    while not acertou:
        try:
            chute = int(input("Seu palpite: "))
        except ValueError:
            print("Por favor, digite um numero valido!\n")
            continue

        tentativas += 1

        if chute < 1 or chute > 100:
            print("O numero deve estar entre 1 e 100. Tente novamente!\n")
        elif chute < numero_secreto:
            print(f"Muito baixo! Tente um numero maior. (Tentativa {tentativas})\n")
        elif chute > numero_secreto:
            print(f"Muito alto! Tente um numero menor. (Tentativa {tentativas})\n")
        else:
            acertou = True
            print("=" * 40)
            print(f"  🎉 PARABENS! Voce acertou!")
            print(f"  O numero secreto era: {numero_secreto}")
            print(f"  Numero de tentativas: {tentativas}")
            if tentativas <= 5:
                print("  Excelente! Voce e muito bom nisso! 🏆")
            elif tentativas <= 10:
                print("  Bom trabalho! 👍")
            else:
                print("  Continua praticando! 💪")
            print("=" * 40)

    jogar_novamente = input("\nDeseja jogar novamente? (s/n): ").lower()
    if jogar_novamente == 's':
        jogo_adivinhacao()
    else:
        print("\nObrigado por jogar! Ate a proxima! 👋")

if __name__ == "__main__":
    jogo_adivinhacao()
