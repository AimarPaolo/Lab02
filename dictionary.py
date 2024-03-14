class Dictionary:
    def __init__(self, dict={}):
        self._dict = dict

    def addWord(self):
        pass

    def translate(self):
        pass

    def translateWordWildCard(self):
        pass
    def loadDictionary(self):
        """
        it loads the dictionary that we are reading at the moment in order to make operations in it
        :return: None
        """
        file_path = 'dictionary.txt'

        with open(file_path, 'r') as file:
            for line in file:
                key_value = line.strip().split()
                if len(key_value) == 2:
                    self._dict[key_value[0]] = key_value[1]
        print(self._dict)
    def printAll(self):
        """stampa tutti i valori contenuti nel dizionario
        :return None"""
        for key, value in self._dict.items():
            alienWord = key
            italianWord = value
            print(f"Alien Word: {alienWord}, Traslation: {italianWord}\n")
