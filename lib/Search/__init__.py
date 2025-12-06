import os
import pandas as pd


class Search:
    """Procura por uma query no arquivo `passwords.csv` e retorna uma lista de tuplas
    (address, user, password) em `self.results`.
    """
    def __init__(self, query: str, csv_file: str = 'passwords.csv'):
        self.query = (query or '').strip()
        self.csv_file = csv_file
        self.results = []
        self.search_passwords()

    def search_passwords(self):
        if not os.path.exists(self.csv_file):
            return
        try:
            df = pd.read_csv(self.csv_file, sep=';', dtype=str).fillna('')
            q = self.query.lower()
            for _, row in df.iterrows():
                addr = str(row.get('Address', '')).strip()
                user = str(row.get('User', '')).strip()
                pwd = str(row.get('Password', '')).strip()
                if q == '':
                    self.results.append((addr, user, pwd))
                else:
                    if q in addr.lower() or q in user.lower() or q in pwd.lower():
                        self.results.append((addr, user, pwd))
        except Exception as e:
            print(f"Error searching passwords: {e}")

