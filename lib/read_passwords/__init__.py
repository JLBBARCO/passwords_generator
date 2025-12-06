import pandas as pd
import threading
import time

class PasswordLoader:

    def __init__(self, app_instance):
        self.app = app_instance
        self.data_loaded = False
        self.passwords_data = []
        self.status_message = "Initialization..."
        self.ErrorFileNotFound = "File Not Found"
        self.loading_thread = None
        self.start_loading()

    def load_data(self):
        try:
            self.status_message = "Changing passwords..."
            if hasattr(self.app, 'update_status'):
                self.app.after(0, lambda: self.app.update_status(self.status_message))
            time.sleep(1)
            with open('passwords.csv', 'r', encoding='utf-8', newline='') as f:
                reader = pd.read_csv(f, sep=';')
                self.passwords_data = reader.to_dict('records')
            self.data_loaded = True
            self.status_message = f"{len(self.passwords_data)} passwords changed successfully!"
            time.sleep(1)
        except FileNotFoundError:
            self.status_message = self.ErrorFileNotFound
        except Exception as e:
            self.status_message = f"Error to change data: {e}"
        if hasattr(self.app, 'after'):
            self.app.after(0, self.app.on_data_loaded)

    def start_loading(self):
        self.loading_thread = threading.Thread(target=self.load_data, daemon=True)
        self.loading_thread.start()

    @property
    def address(self):
        return [record.get('Address', '') for record in self.passwords_data]

    @property
    def user(self):
        return [record.get('User', '') for record in self.passwords_data]

    @property
    def password(self):
        return [record.get('Password', '') for record in self.passwords_data]

    @property
    def all_data(self):
        return self.passwords_data