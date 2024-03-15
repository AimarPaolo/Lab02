class Dictionary:
    def __init__(self, dict={}):
        self._dict = dict

    def addWord(self, key_value):
        if len(key_value) == 2:
            if key_value[0] not in self._dict:
                self._dict[key_value[0]] = key_value[1]
            else:
                val_prec = self._dict.get(key_value[0])
                if isinstance(val_prec, str):
                    currentVal = []
                    currentVal.append(val_prec)
                else:
                    currentVal = self._dict.get(key_value[0])
                print(currentVal)
                self._dict[key_value[0]] = [*currentVal, key_value[1]]
                print(self._dict[key_value[0]])

    def translate(self, key):
        return self._dict.get(key)

    def translateWordWildCard(self):
        pass

    def loadDictionary(self, txtDict):
        """
        it loads the dictionary that we are reading at the moment in order to make operations in it
        :return: None
        """
        with open(txtDict, 'r') as file:
            for line in file:
                key_value = line.strip().split()
                if len(key_value) == 2:
                    self._dict[key_value[0]] = key_value[1]
        print(self._dict)
    def printAll(self):
        """it prints all words in the dictionary
        :return None"""
        for key, value in self._dict.items():
            alienWord = key
            italianWord = value
            print(f"Alien Word: {alienWord}, Traslation: {italianWord}\n")
