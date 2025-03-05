from random import *

def __init__():
    inInicio = int(input("Escolha o que você deseja fazer:\n1. Jogar\n2. Sair\n"))
    if inInicio == 1:
        jogo()
    elif inInicio == 2:
        exit()
    else:
        print("Por favor, insira uma resposta válida.")
        __init__()
        
        
def jogarNovamente():
    inNovamente = int(input("Deseja jogar novamente?\n1.Sim\n2.Não\n"))
    if inNovamente == 1:
        print("Iniciando novamente...")
        jogo()
    elif inNovamente == 2:
        print("Finalizando programa...")
        exit()
    else:
        print("Escolha inválida.")
        jogarNovamente()


def jogo ():
    valor = randint(1, 3)
    usuario = int(input("Escolha qual a sua jogada:\n1. Pedra\n2. Papel\n3. Tesoura\n"))
    
    if valor == 1:
        if usuario == 1:
            print("Empate!\nA escolha do programa também foi pedra!")
            jogarNovamente()
        elif usuario == 2:
            print("Você ganhou!\nA escolha do programa foi pedra!")
            jogarNovamente()
        elif usuario == 3:
            print("Você perdeu!\n A escolha do programa foi pedra!")
            jogarNovamente()
        else:
            print("Escolha inválida, retornando ao inicio.")
            jogarNovamente()
    
    if valor == 2:
        if usuario == 1:
            print("Você perdeu!\nA escolha do programa foi papel!")
            jogarNovamente()
        elif usuario == 2:
            print("Empate!\nA escolha do programa também foi papel!")
            jogarNovamente()
        elif usuario == 3:
            print("Você ganhou!\nA escolha do programa foi papel!")
            jogarNovamente()
        else:
            print("Escolha inválida, retornando ao inicio.")
            jogarNovamente()
            
    if valor == 3:
        if usuario == 1:
            print("Você ganhou!\nA escolha do programa foi tesoura!")
            jogarNovamente()
        elif usuario == 2:
            print("Você perdeu!\nA escolha do programa foi tesoura!")
            jogarNovamente()
        elif usuario == 3:
            print("Empate!\nA escolha do programa também foi tesoura!")
            jogarNovamente()
        else:
            print("Escolha inválida, retornando ao inicio.")
            jogarNovamente()
    

__init__()