import translator as tr

t = tr.Translator()

while True:

    t.printMenu()

    t.loadDictionary("dictionary.txt")

    txtIn = input()

    # Add input control here!

    if int(txtIn) == 1:
        tupla = tuple
        print("Inserire la parola che si vuole aggiungere:")
        txtIn = input()
        try:
            tupla = (txtIn.split(" ")[0], txtIn.split(" ")[1])
        except:
            print("errore")
            continue
        t.handleAdd(tupla)
        print("nuova tupla aggiunta: ", tupla)
        continue
    if int(txtIn) == 2:
        continue
    if int(txtIn) == 3:
        continue
    if int(txtIn) == 4:
        break
