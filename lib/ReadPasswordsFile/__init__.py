import pandas as pd

class ReadPasswordsFile():
    with open('passwords.csv', 'r') as file:
        passwords = pd.read_csv(file, sep=';')
        passwords.columns = passwords.columns.str.strip()

    address = list()
    for item in passwords['Address']:
        address.append(f'{item}\n')
    user = list()
    for item in passwords['User']:
        user.append(f'{item}\n')
    password = list()
    for item in passwords['Password']:
        password.append(f'{item}\n')