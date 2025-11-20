from random import choice
import lib.TypeWindow as TypeWindow

class GenerateComplexPassword(TypeWindow.TypeWindow):
    def __init__(self):
        super().__init__(Address=False, User=False, Password=False, TitleWindow='Generate Complex Password', Characters=True)
        self.password = None

    def submit(self):
        length = self.charactersEntry.get()
        try:
            length = int(length)
            if length <= 0:
                raise ValueError
            caracteres = (
                '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                'A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g',
                'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n',
                'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u',
                'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z',
                '?', '!', '@', '#', '$', '%', '/', '+', '-', '_', '=', '*', '&', '<',
                '>', '(', ')', '[', ']', '{', '}', 'Ç', 'ç'
            )
            self.password = ''.join(choice(caracteres) for _ in range(length))
        except ValueError:
            self.password = 'Invalid length'
        self.destroy()