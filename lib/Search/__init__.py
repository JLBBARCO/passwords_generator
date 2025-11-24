from lib import ReadPasswordsFile

class Search(ReadPasswordsFile.ReadPasswordsFile):
    def __init__(self, query):
        super().__init__()
        self.query = query
        self.results = []
        self.search_passwords()

    def search_passwords(self):
        for addr, user, pwd in zip(self.address, self.user, self.password):
            if self.query.lower() in addr.lower() or self.query.lower() in user.lower() or self.query.lower() in pwd.lower():
                self.results.append((addr.strip(), user.strip(), pwd.strip()))
