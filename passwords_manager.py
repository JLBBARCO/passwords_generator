import customtkinter as ctk

padXMain = 20
padYMain = 10
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Passwords Manager')

        self.main_frame = ctk.CTkFrame(self, width=250, height=250)
        self.main_frame.grid(row=0, column=0, padx=10, pady=10)

        self.textTitle = ctk.CTkLabel(self.main_frame, text='Passwords Manager')
        self.textTitle.grid(row=0, column=0, columnspan=3, padx=padXMain, pady=padYMain)

        self.showTable = ctk.CTkScrollableFrame(self.main_frame, width=750, height=100)
        self.showTable.grid(row=2, column=0, columnspan=3, padx=padXMain, pady=padYMain)

        self.showAddress = ctk.CTkFrame(self.showTable)
        self.showAddress.grid(row=0, column=0, padx=padXMain, pady=padYMain)
        self.showUser = ctk.CTkFrame(self.showTable)
        self.showUser.grid(row=0, column=1, padx=padXMain, pady=padYMain)
        self.showPassword = ctk.CTkFrame(self.showTable)
        self.showPassword.grid(row=0, column=2, padx=padXMain, pady=padYMain)

        self.showTableTitleAddress = ctk.CTkLabel(self.showAddress, text='Address')
        self.showTableTitleAddress.grid(row=0, column=0, padx=padXMain, pady=padYMain)
        self.showTableTitleUser = ctk.CTkLabel(self.showUser, text='User')
        self.showTableTitleUser.grid(row=0, column=0, padx=padXMain, pady=padYMain)
        self.showTableTitlePassword = ctk.CTkLabel(self.showPassword, text='Password')
        self.showTableTitlePassword.grid(row=0, column=0, padx=padXMain, pady=padYMain)

        self.buttonRemove = ctk.CTkButton(self.main_frame, text='Remove', command=self.remove)
        self.buttonRemove.grid(row=3, column=0, padx=padXMain, pady=padYMain)

        self.buttonAdd = ctk.CTkButton(self.main_frame, text='Add', command=self.add)
        self.buttonAdd.grid(row=3, column=2, padx=padXMain, pady=padYMain)

        self.areaGenerate = ctk.CTkFrame(self)
        self.areaGenerate.grid(row=1, column=0, padx=padXMain, pady=padYMain)

        self.buttonGenerateSimplePassword = ctk.CTkButton(self.areaGenerate, text='Generate a Simple Password', command=self.simplePassword)
        self.buttonGenerateSimplePassword.grid(row=0, column=0, padx=padXMain, pady=padYMain)
        self.buttonGenerateComplexPassword = ctk.CTkButton(self.areaGenerate, text='Generate a Complex Password', command=self.complexPassword)
        self.buttonGenerateComplexPassword.grid(row=0, column=1, padx=padXMain, pady=padYMain)

    def remove(self):
        from lib import RemovePassword

    def add(self):
        from lib import AddPassword

    def simplePassword(self):
        from lib import GenerateSimplePassword

    def complexPassword(self):
        from lib import GenerateComplexPassword

app = App()
app.mainloop()