import pyperclip

class Copy:
    @staticmethod
    def copy_to_clipboard(text):
        """Copia o texto para a área de transferência"""
        try:
            pyperclip.copy(text)
            return True
        except Exception as e:
            print(f"Erro ao copiar: {e}")
            return False
