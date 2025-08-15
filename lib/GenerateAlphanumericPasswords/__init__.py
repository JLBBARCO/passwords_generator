# Importações
import random
from lib import ui

# Programa Principal
max_chars = int(input('Digite a quantidade de caracteres: '))
password = list()
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
    ui.resultado(valor=c)
