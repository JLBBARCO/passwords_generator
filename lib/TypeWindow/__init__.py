import customtkinter as ctk

padMain = 5
class TypeWindow(ctk.CTk):
    def __init__(self, TitleWindow='Add Password', Address=False, User=False, Password=False, Characters=False):
        super().__init__()
        self.title(TitleWindow)

        self.main_frame = ctk.CTkFrame(self, width=250, height=150)
        self.main_frame.grid(row=0, column=0, padx=padMain, pady=padMain)

        self.titleLabel = ctk.CTkLabel(self.main_frame, text=TitleWindow)
        self.titleLabel.grid(row=0, column=0, columnspan=2, padx=padMain, pady=padMain)

        if Address:
            self.addressLabel = ctk.CTkLabel(self.main_frame, text='Address:')
            self.addressLabel.grid(row=1, column=0, padx=padMain, pady=padMain)
            self.addressEntry = ctk.CTkEntry(self.main_frame, placeholder_text='Address', width=200)
            self.addressEntry.grid(row=1, column=1, padx=padMain, pady=padMain)
            AddressType = self.addressEntry.get()

        if User:
            self.userLabel = ctk.CTkLabel(self.main_frame, text='User:')
            self.userLabel.grid(row=2, column=0, padx=padMain, pady=padMain)
            self.userEntry = ctk.CTkEntry(self.main_frame, placeholder_text='User', width=200)
            self.userEntry.grid(row=2, column=1, padx=padMain, pady=padMain)
            UserType = self.userEntry.get()

        if Password:
            self.passwordLabel = ctk.CTkLabel(self.main_frame, text='Password:')
            self.passwordLabel.grid(row=3, column=0, padx=padMain, pady=padMain)
            self.passwordEntry = ctk.CTkEntry(self.main_frame, placeholder_text='Password', width=200)
            self.passwordEntry.grid(row=3, column=1, padx=padMain, pady=padMain)
            PasswordType = self.passwordEntry.get()

        if Characters:
            self.charactersLabel = ctk.CTkLabel(self.main_frame, text='Characters:')
            self.charactersLabel.grid(row=4, column=0, padx=padMain, pady=padMain)
            self.charactersEntry = ctk.CTkEntry(self.main_frame, placeholder_text='Characters', width=200)
            self.charactersEntry.grid(row=4, column=1, padx=padMain, pady=padMain)
            CharactersType = self.charactersEntry.get()

        self.submitButton = ctk.CTkButton(self.main_frame, text='Submit', command=self.submit)
        self.submitButton.grid(row=4, column=0, columnspan=2, padx=padMain, pady=padMain)

    def submit(self):
        self.address = self.addressEntry.get() if hasattr(self, 'addressEntry') else None
        self.user = self.userEntry.get() if hasattr(self, 'userEntry') else None
        self.password = self.passwordEntry.get() if hasattr(self, 'passwordEntry') else None
        self.destroy()

app = TypeWindow()
app.mainloop()