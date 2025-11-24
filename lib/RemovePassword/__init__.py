import pandas as pd
import os

class RemovePassword:
    def __init__(self):
        self.csv_file = 'passwords.csv'

    def remove_password(self, address, user):
        """Remove password from CSV file by address and user"""
        try:
            if not os.path.exists(self.csv_file):
                return False

            # Read file
            df = pd.read_csv(self.csv_file, sep=';')
            df.columns = df.columns.str.strip()

            # Find and remove line
            initial_len = len(df)
            df = df[~((df['Address'].str.strip() == address.strip()) & (df['User'].str.strip() == user.strip()))]

            if len(df) < initial_len:
                # Save file actualized
                df.to_csv(self.csv_file, sep=';', index=False)
                return True
            return False
        except Exception as e:
            print(f'Error removing password: {str(e)}')
            return False
