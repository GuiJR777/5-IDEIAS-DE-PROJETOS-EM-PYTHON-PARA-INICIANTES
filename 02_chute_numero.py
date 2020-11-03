'''2. CHUTE O NÚMERO
Objetivo: Criar um script que gerá um valor aleatoriamente, guardar este valor, 
e perguntar repetidamente para o usuário chutar o valor gerado até que ele acerte.

Habilidades praticas a aplicar:

-Random
-Comparadores matemáticos
-Controle de Fluxo
-Entrada de dados
-Saida de dados

Detalhes e boas Práticas: Você deve criar um projeto para rodar na linha de comando que ao iniciar,
irá gerar, armazenar, porem não exibir um valor aleatório entre um valor mínimo e máximo que será 
definido por você ( 10-100, por exemplo). Com esse valor gerado e armazenado de alguma forma que 
você (o criador ou jogador do script) não possa ver, faça uma pergunta do tipo: “Chute um número” 
para quem estiver rodando o script e com isso o programa deve gravar a resposta que foi passada.

Depois disso você terá 3 caminhos possíveis: 1. Avisar que a pessoa chutou baixo, 2 dizer que chutou
alto ou parabenizar dizer que acertou! Considerando os três possíveis caminhos que podem ser seguidos,
você deve cuidar para que em todo o momento a entrada de dados seja tratado para exceções e que caso 
o usuário digite algo inesperado, que ele receba uma mensagem amigável o informando das possíveis opções 
que seu programa oferece. Isso deve continuar acontecendo indefinitivamente até que a pessoa acerte o 
número ou desista por não conseguir acertar hahaha(acontece).'''

import random
from time import sleep

def sorteia(min, max):
    sorteado = random.randint(int(min),int(max))
    return sorteado

def compara(numero_player, numero_sorteado):
    if numero_player > numero_sorteado:
        print('Errou, tente um numero menor.') 
        resultado = False
    elif numero_player < numero_sorteado:
        print('Errou, tente um numero maior.') 
        resultado = False
    elif numero_player == numero_sorteado:
        print('Você acertou!') 
        resultado = True
    return resultado

# Inicio do programa
print('Olá, qual é o seu nome?')
sleep(1)
player = input('Seu nome: ')
pontuacao_geral = 0
sleep(2)
print(f'Prazer em te conhecer { player } ')
sleep(1)
jogar = True
while jogar == True:
    print(f'Seu placar atual é {pontuacao_geral} pontos, Você quer jogar adivinhe o numero? ')
    sleep(2)
    print('Sim (1)')
    print('Não (2)')
    try:
        resposta = int(input('Sua resposta: '))
        if resposta == 1:
            print('Beleza')
            sleep(1)
            print('Vou sortear um número de 1 a 100, você tem 10 tentativas para acertar, você recebe pontos de acordo com quantas tentativas você usou para acertar, Boa Sorte!')
            sleep(1)
            for i in range(5):
                print('=>'*15)
                sleep(1)
            sorteado = int(sorteia(1, 100))
            print('Pronto, agora tente adivinhar!')
            sleep(1)
            comparacao = False
            pontuacao_rodada = 10
            while comparacao == False:
                try:
                    player_numero = int(input('Sua resposta: '))
                except:
                    print('Resposta invalida, tente de novo')
                comparacao= compara(player_numero, sorteado)
                if comparacao == False and pontuacao_rodada > 0:
                    pontuacao_rodada = pontuacao_rodada-1
                elif comparacao == False and pontuacao_rodada == 0:
                    print('Você não conseguiu em 10 tentativas, que pena, vamos começar denovo')
                    comparacao = True
                elif comparacao == True and pontuacao_rodada > 0:
                    pontuacao_geral = pontuacao_geral + pontuacao_rodada
                    print(f'Parabéns, você ganhou {pontuacao_rodada} pontos nessa rodada, seu placar geral agora é {pontuacao_geral}')
                    for i in range(5):
                        print('=>'*15)
                        sleep(1)
                

        elif resposta == 2:
            jogar = False
            print(f'Ok, tchau { player }!')
    except:
        print('Resposta invalida, tente de novo')
        