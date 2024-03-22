import translator as tr

t = tr.Translator()

while True:

    t.printMenu()

    t.loadDictionary("dictionary.txt")
    try:
        txtIn = input()
    except:
        raise ValueError

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
        print("Inserire la parola che si vuole tradurre: ")
        txtIn = input()
        try:
            print("la parola tradotta è:", t.handleTranslate(txtIn))
        except:
            print("parola inserita non presente nel dizionario o errata")
        continue
    if int(txtIn) == 3:
        lista = []
        print("Inserire la parola che si vuole tradurre in formato WildCard: ")
        txtIn = input()
        #try:
        lista = t.handleWildCard(txtIn)
        if len(lista) == 1:
             print("la parola tradotta è: ", t.handleWildCard(txtIn)[0])
        else:
             print("le parole tradotte sono: ")
             for i in range(len(lista)):
                 print(f"{i+1}) : " + lista[i])
      #  except:
          #  print("parola inserita non presente nel dizionario o errata")
        continue
    if int(txtIn) == 4:
        print("stampa di tutto il dizionario presente nel database: ")
        t.handlePrintAll()
        continue
    if int(txtIn) == 5:
        break
