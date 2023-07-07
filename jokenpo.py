from time import sleep
import random
nome = ' JOKENPO! '
pedra = 0
papel = 1
tesoura = 2
print('{:=^20}'.format(nome))
print("")
jogada = ''
r = 'S'
while r == 'S':
    print('''Suas opções:

    [ 0 ] PEDRA
    [ 1 ] PAPEL
    [ 2 ] TESOURA
    ''')
    jogador = int(input("Qual é a sua jogada? "))
    sleep(0.5)
    print("")
    print("JO")
    sleep(0.5)
    print("KEN")
    sleep(0.5)
    print("PO!!")
    sleep(0.5)
    print("")

    jokenpo = [0, 1, 2]

    computador = random.choice(jokenpo)

    if computador == 0 and jogador == 1:
        print("-=-" * 10)
        print("Computador jogou Pedra")
        print("Jogador jogou Papel")
        print("-=-" * 10)
        print("VOCÊ \033[1;32;40mVENCEU\033[m!")
        print("")
        r = str(input("Deseja jogar novamente? [S/N]: ")).upper().strip()
        if r != 'S' and r != 'N':
            r = str(input("Digite apenas 'S' ou 'N': ")).upper().strip()

    elif computador == 0 and jogador == 2:
        print("-=-" * 10)
        print("Computador jogou Pedra")
        print("Jogador jogou Tesoura")
        print("-=-" * 10)
        print("\033[1;31;40mVocê PERDEU\033[m!")
        print("")
        r = str(input("Deseja jogar novamente? [S/N]: ")).upper().strip()
        if r != 'S' and r != 'N':
            r = str(input("Digite apenas 'S' ou 'N': ")).upper().strip()

    elif computador == 1 and jogador == 0:
        print("-=-" * 10)
        print("Computador jogou Papel")
        print("Jogador jogou Pedra")
        print("-=-" * 10)
        print("\033[1;31;40mVocê PERDEU\033[m!")
        print("")
        r = str(input("Deseja jogar novamente? [S/N]: ")).upper().strip()
        if r != 'S' and r != 'N':
            r = str(input("Digite apenas 'S' ou 'N': ")).upper().strip()

    elif computador == 1 and jogador == 2:
        print("-=-" * 10)
        print("Computador jogou Papel")
        print("Jogador jogou Tesoura")
        print("-=-" * 10)
        print("\033[1;32;40mVocê VENCEU\033[m!")
        print("")
        r = str(input("Deseja jogar novamente? [S/N]: ")).upper().strip()
        if r != 'S' and r != 'N':
            r = str(input("Digite apenas 'S' ou 'N': ")).upper().strip()

    elif computador == 2 and jogador == 0:
        print("-=-" * 10)
        print("Computador jogou Tesoura")
        print("Jogador jogou Pedra")
        print("-=-" * 10)
        print("\033[1;32;40mVocê VENCEU\033[m!")
        print("")
        r = str(input("Deseja jogar novamente? [S/N]: ")).upper().strip()
        if r != 'S' and r != 'N':
            r = str(input("Digite apenas 'S' ou 'N': ")).upper().strip()

    elif computador == 2 and jogador == 1:
        print("-=-" * 10)
        print("Computador jogou Tesoura")
        print("Jogador jogou Papel")
        print("-=-" * 10)
        print("Você \033[1;31;40mPERDEU\033[m!")
        print("")
        r = str(input("Deseja jogar novamente? [S/N]: ")).upper().strip()
        if r != 'S' and r != 'N':
            r = str(input("Digite apenas 'S' ou 'N': ")).upper().strip()

    elif computador == jogador:
        print("-=-" * 10)
        print("Ambos jogaram a mesma opção")
        print("-=-" * 10)
        print("\033[1;36;40mEMPATE\033[m!")
        print("")
        r = str(input("Deseja jogar novamente? [S/N]: ")).upper().strip()
        if r != 'S' and r != 'N':
            r = str(input("Digite apenas 'S' ou 'N': ")).upper().strip()

    elif jogador > 2 or jogador < 0:
        print("\033[1;33;40mJogada inválida\033[m.")
        print("")
        r = str(input("Deseja jogar novamente? [S/N]: ")).upper().strip()
        if r != 'S' and r != 'N':
            r = str(input("Digite apenas 'S' ou 'N': ")).upper().strip()
