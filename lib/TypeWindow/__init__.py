import customtkinter as ctk

padMain = 10

class TypeWindow(ctk.CTkToplevel):
    def __init__(self, TitleWindow='Add Password', Address=False, User=False, Password=False, Characters=False, generated_password=None):
        super().__init__()
        self.title(TitleWindow)
        self.resizable(False, False)
        self.geometry('400x350')
        
        # Inicializar variáveis
        self.address = None
        self.user = None
        self.password = None
        self.characters = None
        self.generated_password = generated_password

        # Criar frame principal
        self.main_frame = ctk.CTkFrame(self, width=380, height=330)
        self.main_frame.pack(padx=10, pady=10, fill='both', expand=True)

        # Título
        self.titleLabel = ctk.CTkLabel(self.main_frame, text=TitleWindow, font=('Arial', 14, 'bold'))
        self.titleLabel.pack(padx=padMain, pady=padMain)

        # Address
        if Address:
            address_frame = ctk.CTkFrame(self.main_frame)
            address_frame.pack(padx=padMain, pady=5, fill='x')
            self.addressLabel = ctk.CTkLabel(address_frame, text='Address:', width=100)
            self.addressLabel.pack(side='left', padx=5)
            self.addressEntry = ctk.CTkEntry(address_frame, placeholder_text='Address', width=200)
            self.addressEntry.pack(side='left', padx=5, fill='x', expand=True)

        # User
        if User:
            user_frame = ctk.CTkFrame(self.main_frame)
            user_frame.pack(padx=padMain, pady=5, fill='x')
            self.userLabel = ctk.CTkLabel(user_frame, text='User:', width=100)
            self.userLabel.pack(side='left', padx=5)
            self.userEntry = ctk.CTkEntry(user_frame, placeholder_text='User', width=200)
            self.userEntry.pack(side='left', padx=5, fill='x', expand=True)

        # Password
        if Password:
            password_frame = ctk.CTkFrame(self.main_frame)
            password_frame.pack(padx=padMain, pady=5, fill='x')
            self.passwordLabel = ctk.CTkLabel(password_frame, text='Password:', width=100)
            self.passwordLabel.pack(side='left', padx=5)
            self.passwordEntry = ctk.CTkEntry(password_frame, placeholder_text='Password', width=200)
            self.passwordEntry.pack(side='left', padx=5, fill='x', expand=True)

        # Characters
        if Characters:
            characters_frame = ctk.CTkFrame(self.main_frame)
            characters_frame.pack(padx=padMain, pady=5, fill='x')
            self.charactersLabel = ctk.CTkLabel(characters_frame, text='Characters:', width=100)
            self.charactersLabel.pack(side='left', padx=5)
            self.charactersEntry = ctk.CTkEntry(characters_frame, placeholder_text='Characters', width=200)
            self.charactersEntry.pack(side='left', padx=5, fill='x', expand=True)

        # Senha gerada (read-only)
        if self.generated_password:
            gen_frame = ctk.CTkFrame(self.main_frame)
            gen_frame.pack(padx=padMain, pady=5, fill='x')
            self.generatedLabel = ctk.CTkLabel(gen_frame, text='Generated:', width=100)
            self.generatedLabel.pack(side='left', padx=5)
            self.generatedDisplay = ctk.CTkLabel(gen_frame, text=self.generated_password, fg_color='gray30', corner_radius=5, padx=10, pady=5)
            self.generatedDisplay.pack(side='left', padx=5, fill='x', expand=True)

        # Frame para botões
        button_frame = ctk.CTkFrame(self.main_frame)
        button_frame.pack(padx=padMain, pady=20)

        self.submitButton = ctk.CTkButton(button_frame, text='Submit', command=self.submit, width=100)
        self.submitButton.pack(side='left', padx=5)

        self.cancelButton = ctk.CTkButton(button_frame, text='Cancel', command=self.destroy, width=100)
        self.cancelButton.pack(side='left', padx=5)

    def submit(self):
        if hasattr(self, 'addressEntry'):
            self.address = self.addressEntry.get()
        if hasattr(self, 'userEntry'):
            self.user = self.userEntry.get()
        if hasattr(self, 'passwordEntry'):
            self.password = self.passwordEntry.get()
        elif self.generated_password:
            self.password = self.generated_password
        if hasattr(self, 'charactersEntry'):
            self.characters = self.charactersEntry.get()
        self.destroy()
