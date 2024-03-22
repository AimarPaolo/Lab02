import dictionary

dizio = dictionary.Dictionary()


class Translator:
    def __init__(self, dizionario={}):
        self._dizionario = dizionario

    def printMenu(self):
        # 1. Aggiungi nuova parola
        # 2. Cerca una traduzione
        # 3. Cerca con wildcard
        # 4. Exit
        print("______________________________\n" +
              "   Translator Alien-Italian\n" +
              "______________________________\n" +
              "1. Aggiungi nuova parola\n" +
              "2. Cerca una traduzione\n" +
              "3. Cerca con wildcard\n" +
              "4. Stampa tutto il Dizionario\n" +
              "5. Exit\n" +
              "______________________________\n")

    def loadDictionary(self, nome_file):
        # dict is a string with the filename of the dictionary
        self._dizionario = dizio.loadDictionary(nome_file)

    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
       # self._dizionario[entry[0]] = entry[1]
        dizio.addWord(entry)

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        return dizio.translate(query)

    def handleWildCard(self, query):
        # query is a string with a ? --> <par?la_aliena>
        return dizio.translateWordWildCard(query)

    def handlePrintAll(self):
        dizio.printAll()