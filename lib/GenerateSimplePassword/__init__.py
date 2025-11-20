from random import randint
import lib.TypeWindow as TypeWindow

class GenerateSimplePassword(TypeWindow.TypeWindow('Type of Number of Characters', Characters=True)):
    def __init__(self):
        super().__init__(Address=False, User=False, Password=True, TitleWindow='Generate Simple Password')
        self.mainloop()

    def submit(self):
        length = self.passwordEntry.get()
        try:
            length = int(length)
            if length <= 0:
                raise ValueError
            characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
            password = ''.join(characters[randint(0, TypeWindow.CharactersType - 1)] for _ in range(length))
            self.password = password
        except ValueError:
            self.password = 'Invalid length'
        self.destroy()