'''1. SIMULADOR DE DADO
Objetivo: Seu script deve gerar um valor aleatório entre 1 e 6(ou uma faixa que você definir) e permitir que o usuário rode o script quantas vezes quiser.

Habilidades praticas a aplicar:

Tratamento de exceções
Condicionais If/Else
Input de dados
Geração de valores
Print
Detalhes e boas Práticas: Você deve desenvolver um projeto em Python que irá rodar inicialmente na linha de comando e que, ao ser executado, deverá pergunta o seguinte ao usuário: “Você gostaria de jogar o dado?” Ou alguma variação dessa pergunta. Depois de ter feito essa pergunta, o seu programa precisa avaliar a resposta que foi digitado pelo usuário.

Um passo importante aqui é que, quando digo avaliar quero dizer que você precisa receber o valor, tratar quando ele(a) disser que sim ou que não. Seu programa depois deverá fazer a ação necessária de acordo com a resposta que foi entrada pelo usuário. Seu script não deve quebrar ou para de funcionar caso o usuário entre algo que não seja esperado, como, por exemplo, um número. Trate as exceções ou erros para que seu script rode liso e sem problemas.

Caso a resposta a pergunta inicial tenha sido “sim” ou positiva de alguma forma, gere um valor aleatoriamente entre 1 e 6(você pode claro alterar essa faixa) e exiba o número no console para o usuário. Na sequência pergunte se ele(a) quer rodar o script novamente e trate essa situação para que continue rodando enquanto a resposta for positiva, fechando apenas quando for um “não”.

'''

import random
from time import sleep


class SimuladorDados:
    def __init__(self):
        self.__dados = [4, 6, 8, 10, 12, 20, 100]

    def lanca_dado(self, tipo: int, quantidade_de_dados: int = 1):
        valor_max = tipo
        lancamentos = quantidade_de_dados
        resultados = []
        retorno = None
        if lancamentos > 1:
            for dado in range(lancamentos):
                resultado = random.randint(1, valor_max)
                print(f'O dado {dado+1} deu: {resultado}')
                resultados.append(resultado)
                retorno = resultados
        else:
            resultado = random.randint(1, valor_max)
            print(f'Resultado: {resultado}')
            retorno = resultado

        return retorno

    def soma_resultado(self, lista):
        soma = 0
        for i in lista:
            soma = soma + int(i)
        return soma

    def execute(self):
        print('Olá, qual é o seu nome?')
        sleep(1)
        player = input('Seu nome: ')
        sleep(2)
        print(f'Prazer em te conhecer { player }')
        sleep(1)
        lancar = True
        while lancar == True:
            print('Você quer lançar um dado? ')
            sleep(2)
            print('Sim (1)')
            print('Não (2)')
            try:
                resposta = int(input('Sua resposta: '))
                if resposta == 1:
                    # Seleção de dado
                    print('Vamos Jogar')
                    sleep(1)
                    print('Que tipo de dado você quer lançar?')
                    sleep(2)
                    contador = 0
                    for dado in self.__dados:
                        print(f'D{dado} ({contador})')
                        contador += 1
                        sleep(1)
                    try:
                        tipo = int(input('Sua resposta: '))
                    except:
                        print('Resposta invalida, tente de novo')
                    sleep(2)
                    print(f'Você vai lançar o D{ self.__dados[tipo] }')
                    sleep(1)
                    # Seleção de quantidade
                    print('Quantos dados você quer jogar?')
                    sleep(1)
                    try:
                        qtd = int(
                            input('Sua resposta(deve ser um numero inteiro): '))
                    except:
                        print('Resposta invalida, tente de novo')
                    resultado = self.lanca_dado(self.__dados[tipo], qtd)
                    if type(resultado) == list:
                        resultado = self.soma_resultado(resultado)
                    print(
                        f'Você lançou {qtd} D{self.__dados[tipo]} e obteve {resultado} como resultado')
                    sleep(10)

                elif resposta == 2:
                    lancar = False
                    print('ok')

            except:
                print('Resposta invalida, tente de novo')


if __name__ == '__main__':
    SimuladorDados().execute()
