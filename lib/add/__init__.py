import pandas as pd
import os

class AddPassword:
    def __init__(self):
        self.csv_file = 'passwords.csv'
    
    def add_password(self, address, user, password):
        """Add a new password in CSV file if not exist"""
        try:
            # Read existent file
            if os.path.exists(self.csv_file):
                df = pd.read_csv(self.csv_file, sep=';')
                df.columns = df.columns.str.strip()
            else:
                df = pd.DataFrame(columns=['Address', 'User', 'Password'])

            # Verify if the combination exists
            existing = df[(df['Address'].str.strip() == address.strip()) & (df['User'].str.strip() == user.strip()) & (df['Password'].str.strip() == password.strip())]

            if not existing.empty:
                return False  # Passwords exist

            # Add new line
            new_row = pd.DataFrame([{'Address': address.strip(), 'User': user.strip(), 'Password': password.strip()}])
            df = pd.concat([df, new_row], ignore_index=True)

            # Save file
            df.to_csv(self.csv_file, sep=';', index=False)
            return True
        except Exception as e:
            print(f"Erro ao adicionar senha: {e}")
            return False
