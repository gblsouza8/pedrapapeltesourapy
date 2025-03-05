from random import *


# Função que irá iniciar o programa
def __init__():
    
    # Pergunta e registra a resposta do usuário na variável inInicio 
    inInicio = int(input("Escolha o que você deseja fazer:\n1. Jogar\n2. Sair\n"))
    # Se a resposta do usuário for 1. Jogar, vai iniciar a função de jogo
    if inInicio == 1:
        jogo()
    # Se a resposta do usuário for 2. Sair, vai finalizar o programa
    elif inInicio == 2:
        exit()
    # Se não for nenhuma das duas, vai pedir uma resposta válida e iniciar a função novamente
    else:
        print("Por favor, insira uma resposta válida.")
        __init__()
        
    # Função que irá rodar após o fim do jogo, perguntando se o usuário deseja jogar novamente
def jogarNovamente():
    # Registra a resposta na variável inNovamente
    inNovamente = int(input("Deseja jogar novamente?\n1.Sim\n2.Não\n"))
    # Se for 1, irá iniciar o jogo novamente
    if inNovamente == 1:
        print("Iniciando novamente...")
        jogo()
    # Se for 2, irá sair
    elif inNovamente == 2:
        print("Finalizando programa...")
        exit()
    # Se não for nenhum dos dois, irá dizer que a escolha foi inválida e iniciar novamente a função que pergunta
    else:
        print("Escolha inválida.")
        jogarNovamente()



# Função que roda o jogo
def jogo ():
    # Gera um valor aleatório entre 1 e 3, que simbolizam a Pedra, o Papel e a Tesoura respectivamente.
    valor = randint(1, 3)
    # Pergunta ao usuário qual será a sua jogada e armazena a resposta na variável usuário
    usuario = int(input("Escolha qual a sua jogada:\n1. Pedra\n2. Papel\n3. Tesoura\n"))
    
    
    # Se o valor aleatório for 1, irá rodar uma sequência de ifs verificando se o usuário ganhou ou perdeu, 
    # e rodar o jogarNovamente independente do resultado.
    if valor == 1:
        if usuario == 1:
            print("Empate!\nA escolha do programa também foi pedra!")
            jogarNovamente()
        elif usuario == 2:
            print("Você ganhou!\nA escolha do programa foi pedra!")
            jogarNovamente()
        elif usuario == 3:
            print("Você perdeu!\nA escolha do programa foi pedra!")
            jogarNovamente()
        # Se o usuário escolher um número inválido, irá reiniciar o jogo.
        else:
            print("Escolha inválida, retornando ao inicio.")
            jogo()
    
    # Se o valor aleatório for 2, irá rodar uma sequência de ifs verificando se o usuário ganhou ou perdeu, 
    # e rodar o jogarNovamente independente do resultado.
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
        # Se o usuário escolher um número inválido, irá reiniciar o jogo.
        else:
            print("Escolha inválida, retornando ao inicio.")
            jogo()
            
    # Se o valor aleatório for 3, irá rodar uma sequência de ifs verificando se o usuário ganhou ou perdeu, 
    # e rodar o jogarNovamente independente do resultado.
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
        # Se o usuário escolher um número inválido, irá reiniciar o jogo.
        else:
            print("Escolha inválida, retornando ao inicio.")
            jogo()
    

__init__()