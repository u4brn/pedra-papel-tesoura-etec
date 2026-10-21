import random
def jogar():
    opcoes = ["pedra", "papel", "tesoura"]
    pontos_jogador = 0
    pontos_computador = 0
    while pontos_jogador < 5 and pontos_computador < 5:
        escolha = input("escolha entre pedra, papel ou tesoura: ")
        computador = random.choice(opcoes)
        if escolha not in opcoes:
            print("você só pode escolher entre pedra, papel ou tesoura")
        else:
            print(f"o computador escolheu: {computador}")
            if escolha == computador:
                print("empate")
            elif (escolha == "pedra" and computador == "tesoura") or (escolha == "papel" and computador == "pedra") or (escolha == "tesoura" and computador == "papel"):
                print("você ganhou a rodada!")
                pontos_jogador += 1
            else:
                print("o computador ganhou a rodada!")
                pontos_computador += 1
            print(f"jogador: {pontos_jogador}\ncomputador: {pontos_computador}")
    if pontos_jogador == 5:
        print("você venceu o jogo!")
        continuar = input("você gostaria de jogar novamente? aperte 'enter' se não ou digite 'sim': ")
        if continuar.lower() == "sim":
            jogar()
        else:
            exit()
    else:
        print("o computador venceu o jogo!")
jogar()