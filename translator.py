import dictionary
import dictionary as Dictionary


class Translator:
    def __init__(self, dictionary = Dictionary.Dictionary()):
        self.dictionary = dictionary

    def printMenu(self):
        print("-----------------------------\n"
              "   Translator Alien-Italian\n-----------------------------\n1. Aggiungi nuova parola"
              "\n2. Cerca una traduzione\n3. Cerca con wildcard\n4. Stampa tutto il dizionario\n"
              "5. Exit\n-----------------------------\n")
        pass

    def loadDictionary(self, txtDict):
        self.dictionary.loadDictionary(txtDict)
        pass

    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        pass

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        pass

    def handleWildCard(self, query):
        # query is a string with a ? --> <par?la_aliena>
        pass

    def printAll(self):
        self._dict.printAll()
