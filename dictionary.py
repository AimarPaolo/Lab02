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
                else:
                    prevVal = self._dictionary.get(key_value[0])
                    if isinstance(prevVal, str):
                        currentVal = []
                        currentVal.append(prevVal)
                    else:
                        currentVal = self._dictionary.get(key_value[0])
                    print(currentVal)
                    self._dictionary[key_value[0]] = [*currentVal, key_value[1]]
                    print(self._dictionary[key_value[0]])

    def addWord(self, tupla):
        cont = 0
        self._dictionary[tupla[0]] = tupla[1]
        with open("dictionary.txt", 'w') as f:
            for riga in self._dictionary:
                f.write(f"{riga} {self._dictionary[riga]}\n")

    def translate(self, query):
        return self._dictionary[query]

    def translateWordWildCard(self, parola):
        lista = []
        if '?' in parola:
            indice = parola.find("?")
            parola.replace('?', "")
            for keys in self._dictionary:
                templ = keys
                keys = list(templ)
                if indice >= len(keys):
                    pass
                else:
                    keys[indice] = '?'
                    keys = ''.join(keys)
                    keys.replace('?', "")
                    if keys.__eq__(parola):
                        lista.append(self._dictionary[templ])
        else:
            lista.append(self.translate(parola))
        return lista
    def printAll(self):
        for keys in self._dictionary:
            print(f"{keys} : {self._dictionary[keys]}")