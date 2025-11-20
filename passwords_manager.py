import customtkinter as ctk
from lib import ReadPasswordsFile, TypeWindow

padMain = 25
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Passwords Manager')

        self.main_frame = ctk.CTkFrame(self, width=250, height=250)
        self.main_frame.grid(row=0, column=0, padx=10, pady=10)

        self.textTitle = ctk.CTkLabel(self.main_frame, text='Passwords Manager')
        self.textTitle.grid(row=0, column=0, columnspan=3, padx=padMain, pady=padMain)

        self.showTable = ctk.CTkScrollableFrame(self.main_frame, width=500, height=100)
        self.showTable.grid(row=2, column=0, columnspan=3, padx=padMain, pady=padMain)

        self.showTableTitleAddress = ctk.CTkLabel(self.showTable, text='Address')
        self.showTableTitleAddress.grid(row=0, column=0, padx=padMain, pady=padMain)
        self.showTableTitleUser = ctk.CTkLabel(self.showTable, text='User')
        self.showTableTitleUser.grid(row=0, column=1, padx=padMain, pady=padMain)
        self.showTableTitlePassword = ctk.CTkLabel(self.showTable, text='Password')
        self.showTableTitlePassword.grid(row=0, column=2, padx=padMain, pady=padMain)

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

        self.buttonRemove = ctk.CTkButton(self.main_frame, text='Remove', command=self.remove)
        self.buttonRemove.grid(row=3, column=0, padx=padMain, pady=padMain)

        self.buttonAdd = ctk.CTkButton(self.main_frame, text='Add', command=self.add)
        self.buttonAdd.grid(row=3, column=2, padx=padMain, pady=padMain)

        self.areaGenerate = ctk.CTkFrame(self)
        self.areaGenerate.grid(row=1, column=0, padx=padMain, pady=padMain)

        self.buttonGenerateSimplePassword = ctk.CTkButton(self.areaGenerate, text='Generate a Simple Password', command=self.simplePassword)
        self.buttonGenerateSimplePassword.grid(row=0, column=0, padx=padMain, pady=padMain)
        self.buttonGenerateComplexPassword = ctk.CTkButton(self.areaGenerate, text='Generate a Complex Password', command=self.complexPassword)
        self.buttonGenerateComplexPassword.grid(row=0, column=1, padx=padMain, pady=padMain)

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