class Dictionary:
    def __init__(self, dictionary={}):
        self._dictionary = dictionary

    def loadDictionary(self, nome_file):
        line = []
        with open(nome_file, 'r') as f:
            for line in f:
                key_value = line.strip().split()
                if len(key_value) == 2:
                    self._dictionary[key_value[0]] = key_value[1]
        return self._dictionary

    def addWord(self, tupla):
        cont = 0
        self._dictionary[tupla[0]] = tupla[1]
        with open("dictionary.txt", 'w') as f:
            for riga in self._dictionary:
                f.write(f"{riga} {self._dictionary[riga]}\n")

    def translate(self):
        pass

    def translateWordWildCard(self):
        pass