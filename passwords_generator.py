# Importações
import random
from time import sleep

def linha(tam=60):
    """
    -> Cria uma linha de separação.
    :param tam: O tamanho da linha. Padrão é 60.
    :return: None
    """
    print('-' * tam)

def cabeçalho(txt):
    """
    -> Cria um cabeçalho para o programa.
    :param txt: O texto a ser exibido no cabeçalho.
    :return: None
    """
    linha()
    print(txt.center(60))
    linha()

def menu(opções=[], título='MENU DE OPÇÕES'):
    """
    -> Cria um menu de opções para o programa.
    :param opções: Informações sobre a opção.
    :param título: Título do menu, se não for passado, o padrão é 'MENU DE OPÇÕES'. False para não mostrar o título.
    """
    if título == False:
        pass
    else:
        cabeçalho(título)
    for i, c in enumerate(opções):
        print(f'\033[33m{i}\033[m - \033[34m{c}\033[m')

def resultado(valor, fim='', linhas=True):
    """
    -> Personaliza o return de algum resultado.
    :param valor: Valor do resultado.
    :param fim: Declara qual vai ser o end do print. Padrão vazio.
    :param linhas: Declara se vai mostrar linhas nas partes de cima e baixo do resultado. Padrão True.
    """
    if isinstance(valor, (list, dict, tuple)):
        if linhas is True:
            linha()
        for c in valor:
            print(c, end=fim)
        print()
    else:
        print(valor, end=fim)

def gerador_senha_alphanumérica():
    """
    -> Pede ao usuário a quantidade de caracteres a serem sorteados. O programa sorteia números inteiros e adiciona a uma lista os caracteres referentes ao número sorteado em uma lista de caracteres alphanuméricos pré-definidos.
    """
    max_chars = int(input('Digite a quantidade de caracteres: '))
    password = []
    caracteres = (
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
        'A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g',
        'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n',
        'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u',
        'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z'
    )
    for _ in range(max_chars):
        sorteado = random.randint(0, len(caracteres) - 1)
        password.append(caracteres[sorteado])
    for c in password:
        resultado(valor=c)
    print()

def gerador_senha_alphanumérica_caracteres():
    """
    -> Pede ao usuário a quantidade de caracteres a serem sorteados. O programa sorteia números inteiros e coloca em uma lista os caracteres referentes pré-declarados em uma lista.
    """
    max_chars = int(input('Digite a quantidade de caracteres: '))
    password = []
    caracteres = (
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
        'A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g',
        'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n',
        'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u',
        'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z',
        '?', '!', '@', '#', '$', '%', '/', '+', '-', '_', '=', '*', '&', '<',
        '>', '(', ')', '[', ']', '{', '}', 'Ç', 'ç'
    )
    for _ in range(max_chars):
        sorteado = random.randint(0, len(caracteres) - 1)
        password.append(caracteres[sorteado])
    for c in password:
        resultado(valor=c, linhas=False)
    print()



# Função Principal
"""
-> Mostra as opções de sorteio, pede ao usuário escolher alguma, e executa a função referente a escolha do usuário.
"""
while True:
    opções = [
        'Sair',
        'Gerador de Senhas Alphanuméricas',
        'Gerador de Senhas Alphanuméricas com Caracteres Especiais',
    ]
    menu(opções, 'Gerador de Senhas')
    resposta = input('Escolha: ')
    if resposta == '0':
        cabeçalho('Saindo... Volte Sempre!')
        break

    elif resposta == '1':
        gerador_senha_alphanumérica()

    elif resposta == '2':
        gerador_senha_alphanumérica_caracteres()

    else:
        print('\033[0;31mERRO! Digite uma opção válida.\033[m')
