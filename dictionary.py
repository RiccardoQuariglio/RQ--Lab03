class Dictionary:
    def __init__(self):
        self._dict = []

    def loadDictionary(self,path):
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                self._dict.append(line.lower().rstrip())

    def printAll(self):
        for w in self._dict:
            print(w)


    @property
    def dict(self):
        return self._dict