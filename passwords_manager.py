import customtkinter as ctk
from lib import ReadPasswordsFile

padMain = 10
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Passwords Manager')

        self.main_frame = ctk.CTkFrame(self, width=250, height=250)
        self.main_frame.grid(row=0, column=0, padx=10, pady=10)

        self.textTitle = ctk.CTkLabel(self.main_frame, text='Passwords Manager')
        self.textTitle.grid(row=0, column=0, columnspan=3, padx=padMain, pady=padMain)

        self.SearchBar = ctk.CTkEntry(self.main_frame, placeholder_text='Search')
        self.SearchBar.grid(row=1, column=0, columnspan=2, pady=padMain)

        self.SearchButton = ctk.CTkButton(self.main_frame, text='🔍', command=self.search)
        self.SearchButton.grid(row=1, column=2, pady=padMain)

        self.showTable = ctk.CTkScrollableFrame(self.main_frame, width=500, height=100)
        self.showTable.grid(row=2, column=0, columnspan=3, padx=padMain, pady=padMain)

        self.showTableTitleAddress = ctk.CTkLabel(self.showTable, text='Address')
        self.showTableTitleAddress.grid(row=0, column=0, padx=padMain, pady=padMain)
        self.showTableTitleUser = ctk.CTkLabel(self.showTable, text='User')
        self.showTableTitleUser.grid(row=0, column=1, padx=padMain, pady=padMain)
        self.showTableTitlePassword = ctk.CTkLabel(self.showTable, text='Password')
        self.showTableTitlePassword.grid(row=0, column=2, padx=padMain, pady=padMain)

        try:
            self.counter = 0
            for item in ReadPasswordsFile.ReadPasswordsFile().address:
                self.counter += 1
                self.showInfoAddress = ctk.CTkLabel(self.showTable, text=item)
                self.showInfoAddress.grid(row=self.counter, column=0, padx=padMain, pady=padMain)
            self.counter = 0
            for item in ReadPasswordsFile.ReadPasswordsFile().user:
                self.counter += 1
                self.showInfoAddress = ctk.CTkLabel(self.showTable, text=item)
                self.showInfoAddress.grid(row=self.counter, column=1, padx=padMain, pady=padMain)
            self.counter = 0
            for item in ReadPasswordsFile.ReadPasswordsFile().password:
                self.counter += 1
                self.showInfoAddress = ctk.CTkLabel(self.showTable, text=item)
                self.showInfoAddress.grid(row=self.counter, column=2, padx=padMain, pady=padMain)
        except:
            self.ShowError = ctk.CTkLabel(self.showTable, text=ReadPasswordsFile.ReadPasswordsFile.ErrorFileNotFound)
            self.ShowError.grid(row=1, column=0, columnspan=3, padx=padMain, pady=padMain)

        self.buttonRemove = ctk.CTkButton(self.main_frame, text='Remove', command=self.remove)
        self.buttonRemove.grid(row=3, column=0, padx=padMain, pady=padMain)

        self.buttonAdd = ctk.CTkButton(self.main_frame, text='Add', command=self.add)
        self.buttonAdd.grid(row=3, column=2, padx=padMain, pady=padMain)

        self.areaGenerate = ctk.CTkFrame(self)
        self.areaGenerate.grid(row=1, column=0, columnspan=3, padx=padMain, pady=padMain)

        self.buttonGenerateSimplePassword = ctk.CTkButton(self.areaGenerate, text='Generate a Simple Password', command=self.simplePassword)
        self.buttonGenerateSimplePassword.grid(row=0, column=0, padx=padMain, pady=padMain)
        self.buttonGenerateComplexPassword = ctk.CTkButton(self.areaGenerate, text='Generate a Complex Password', command=self.complexPassword)
        self.buttonGenerateComplexPassword.grid(row=1, column=0, padx=padMain, pady=padMain)

        self.areaPrintPassword = ctk.CTkLabel(self.areaGenerate)

    def search(self):
        from lib.Search import Search
        search_obj = Search(self.SearchBar.get())
        
        # Limpar tabela
        for widget in self.showTable.winfo_children()[3:]:
            widget.destroy()
        
        if search_obj.results:
            self.counter = 1
            for addr, user, pwd in search_obj.results:
                addr_label = ctk.CTkLabel(self.showTable, text=addr)
                addr_label.grid(row=self.counter, column=0, padx=padMain, pady=padMain)
                
                user_label = ctk.CTkLabel(self.showTable, text=user)
                user_label.grid(row=self.counter, column=1, padx=padMain, pady=padMain)
                
                pwd_label = ctk.CTkLabel(self.showTable, text=pwd)
                pwd_label.grid(row=self.counter, column=2, padx=padMain, pady=padMain)
                
                self.counter += 1
        else:
            no_results = ctk.CTkLabel(self.showTable, text='No results found')
            no_results.grid(row=1, column=0, columnspan=3, padx=padMain, pady=padMain)

    def add(self):
        from lib.TypeWindow import TypeWindow
        add_window = TypeWindow(TitleWindow='Add Password', Address=True, User=True, Password=True)
        self.wait_window(add_window)
        
        if add_window.address and add_window.user and add_window.password:
            from lib.AddPassword import AddPassword
            AddPassword().add_password(add_window.address, add_window.user, add_window.password)
            self.reload_table()

    def remove(self):
        from lib.TypeWindow import TypeWindow
        remove_window = TypeWindow(TitleWindow='Remove Password', Address=True, User=True, Password=True)
        self.wait_window(remove_window)
        
        if remove_window.address and remove_window.user and remove_window.password:
            from lib.RemovePassword import RemovePassword
            RemovePassword().remove_password(remove_window.address, remove_window.user, remove_window.password)
            self.reload_table()

    def simplePassword(self):
        from lib.GenerateSimplePassword import GenerateSimplePassword
        app = GenerateSimplePassword()
        self.wait_window(app)

        if app.password:
            if self.areaPrintPassword.winfo_exists():
                self.areaPrintPassword.destroy()
            
            # Frame para conter label e botões
            self.areaPrintPassword = ctk.CTkFrame(self.areaGenerate)
            self.areaPrintPassword.grid(row=0, rowspan=2, column=1, padx=padMain, pady=padMain)
            
            # Label com a senha
            password_label = ctk.CTkLabel(self.areaPrintPassword, text=app.password, fg_color='gray30', padx=10, pady=5)
            password_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
            
            # Botão Copy
            copy_btn = ctk.CTkButton(self.areaPrintPassword, text='Copy', width=60, command=lambda: self.copy_password(app.password))
            copy_btn.grid(row=1, column=0, padx=5, pady=5)
            
            # Botão Save
            save_btn = ctk.CTkButton(self.areaPrintPassword, text='Save', width=60, command=lambda: self.save_password(app.password))
            save_btn.grid(row=1, column=1, padx=5, pady=5)

    def complexPassword(self):
        from lib.GenerateComplexPassword import GenerateComplexPassword
        app = GenerateComplexPassword()
        self.wait_window(app)

        if app.password:
            if self.areaPrintPassword.winfo_exists():
                self.areaPrintPassword.destroy()
            
            # Frame para conter label e botões
            self.areaPrintPassword = ctk.CTkFrame(self.areaGenerate)
            self.areaPrintPassword.grid(row=1, rowspan=1, column=1, padx=padMain, pady=padMain)
            
            # Label com a senha
            password_label = ctk.CTkLabel(self.areaPrintPassword, text=app.password, fg_color='gray30', padx=10, pady=5)
            password_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
            
            # Botão Copy
            copy_btn = ctk.CTkButton(self.areaPrintPassword, text='Copy', width=60, command=lambda: self.copy_password(app.password))
            copy_btn.grid(row=1, column=0, padx=5, pady=5)
            
            # Botão Save
            save_btn = ctk.CTkButton(self.areaPrintPassword, text='Save', width=60, command=lambda: self.save_password(app.password))
            save_btn.grid(row=1, column=1, padx=5, pady=5)

    def copy_password(self, password):
        """Copia a senha para a área de transferência"""
        from lib.Copy import Copy
        if Copy.copy_to_clipboard(password):
            print("Senha copiada com sucesso!")
        else:
            print("Erro ao copiar senha")

    def save_password(self, password):
        """Abre janela para salvar a senha gerada"""
        from lib.TypeWindow import TypeWindow
        save_window = TypeWindow(TitleWindow='Save Generated Password', Address=True, User=True, Password=False, generated_password=password)
        self.wait_window(save_window)
        
        if save_window.address and save_window.user:
            from lib.AddPassword import AddPassword
            if AddPassword().add_password(save_window.address, save_window.user, password):
                print("Senha salva com sucesso!")
                self.reload_table()
            else:
                print("Esta senha já existe!")

    def reload_table(self):
        # Limpar tabela
        for widget in self.showTable.winfo_children()[3:]:
            widget.destroy()
        
        # Recarregar dados
        try:
            passwords_file = ReadPasswordsFile.ReadPasswordsFile()
            self.counter = 1
            for addr, user, pwd in zip(passwords_file.address, passwords_file.user, passwords_file.password):
                addr_label = ctk.CTkLabel(self.showTable, text=addr.strip())
                addr_label.grid(row=self.counter, column=0, padx=padMain, pady=padMain)
                
                user_label = ctk.CTkLabel(self.showTable, text=user.strip())
                user_label.grid(row=self.counter, column=1, padx=padMain, pady=padMain)
                
                pwd_label = ctk.CTkLabel(self.showTable, text=pwd.strip())
                pwd_label.grid(row=self.counter, column=2, padx=padMain, pady=padMain)
                
                self.counter += 1
        except Exception as e:
            error_label = ctk.CTkLabel(self.showTable, text=f'Error: {str(e)}')
            error_label.grid(row=1, column=0, columnspan=3, padx=padMain, pady=padMain)

if __name__ == '__main__':
    app = App()
    app.mainloop()