import pandas as pd

class ReadPasswordsFile():
    ErrorFileNotFound = 'No Password Saved'

    def __init__(self):
        try:
            with open('passwords.csv', 'r') as file:
                passwords = pd.read_csv(file, sep=';')
                passwords.columns = passwords.columns.str.strip()

            self.address = []
            for item in passwords['Address']:
                self.address.append(f'{item}\n')
            self.user = []
            for item in passwords['User']:
                self.user.append(f'{item}\n')
            self.password = []
            for item in passwords['Password']:
                self.password.append(f'{item}\n')
        except FileNotFoundError:
            return ReadPasswordsFile.ErrorFileNotFound
            self.address = []
            self.user = []
            self.password = []
