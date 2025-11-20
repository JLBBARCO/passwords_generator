from random import randint
import lib.TypeWindow as TypeWindow

class GenerateComplexPassword(TypeWindow.TypeWindow('Type of Number of Characters', Characters=True)):
    def __init__(self):
        super().__init__(Address=False, User=False, Password=True, TitleWindow='Generate Complex Password')
        self.mainloop()

    def submit(self):
        length = self.passwordEntry.get()
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
            password = ''.join(caracteres[randint(0, len(caracteres) - 1)] for _ in range(length))
            self.password = password
        except ValueError:
            self.password = 'Invalid length'
        self.destroy()