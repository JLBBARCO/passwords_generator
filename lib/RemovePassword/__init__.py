import pandas as pd
import os

class RemovePassword:
    def __init__(self):
        self.csv_file = 'passwords.csv'
    
    def remove_password(self, address, user, password):
        """Remove uma senha do arquivo CSV"""
        try:
            if not os.path.exists(self.csv_file):
                return False
            
            # Ler arquivo
            df = pd.read_csv(self.csv_file, sep=';')
            df.columns = df.columns.str.strip()
            
            # Encontrar e remover a linha
            initial_len = len(df)
            df = df[~((df['Address'].str.strip() == address.strip()) & 
                      (df['User'].str.strip() == user.strip()) & 
                      (df['Password'].str.strip() == password.strip()))]
            
            if len(df) < initial_len:
                # Salvar arquivo atualizado
                df.to_csv(self.csv_file, sep=';', index=False)
                return True
            return False
        except Exception as e:
            print(f"Erro ao remover senha: {e}")
            return False
