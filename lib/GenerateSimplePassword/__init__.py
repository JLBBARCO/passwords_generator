from random import choice
import lib.TypeWindow as TypeWindow

class GenerateSimplePassword(TypeWindow.TypeWindow):
    def __init__(self):
        super().__init__(Address=False, User=False, Password=False, TitleWindow='Generate Simple Password', Characters=True)
        self.password = None

    def submit(self):
        length = self.charactersEntry.get()
        try:
            length = int(length)
            if length <= 0:
                raise ValueError
            characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
            self.password = ''.join(choice(characters) for _ in range(length))
        except ValueError:
            self.password = 'Invalid length'
        self.destroy()