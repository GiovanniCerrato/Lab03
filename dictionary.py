from email.header import UTF8


class Dictionary:
    def __init__(self):
        self._dict = []

    def loadDictionary(self,path):
        try:
            f = open(f"resources/{path}.txt", "r",encoding="utf-8").read().splitlines()
            self.dict = f
        except FileNotFoundError:
            print("File non trovato!")
        return self.dict


    def printAll(self):
        for word in self.dict:
            print(word)


    @property
    def dict(self):
        return self._dict
    @dict.setter
    def dict(self,value):
        self._dict = value