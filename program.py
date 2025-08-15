# Importações
import random
from lib import ui

# Função Principal
while True:
    opções = [
        'Sair',
        'Gerador de Senhas Alphanuméricas',
        'Gerador de Senhas Alphanuméricas com Caracteres Especiais',
    ]
    ui.menu(opções, 'Gerador de Senhas')
    resposta = input('Escolha: ')
    if resposta == '0':
        ui.cabeçalho('Saindo... Volte Sempre!')
        break

    elif resposta == '1':
        from lib import GenerateAlphanumericPasswords

    elif resposta == '2':
        from lib import GenerateAlphanumericsPasswordsWithSpecialCaracteres

    else:
        print('\033[0;31mERRO! Digite uma opção válida.\033[m')
