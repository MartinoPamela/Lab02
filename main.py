import translator as tr

t = tr.Translator()


while(True):

    t.printMenu()

    t.loadDictionary("dictionary.txt")

    txtIn = input()

    # Add input control here!

    if int(txtIn) == 1:
        print("Ok, quale parola devo aggiungere?")
        txtIn = input().lower()
        t.handleAdd(txtIn)
        print("Aggiunta!")
        continue

    if int(txtIn) == 2:
        print("Ok, quale parola devo cercare?\n")
        txtIn = input()
        txtTransl = t.handleTranslate(txtIn)
        print(txtTransl)
        continue

    if int(txtIn) == 3:
        print("Ok, quale parola devo cercare?\n")
        txtIn = input()
        txtTransl = t.handleWildCard(txtIn)
        print(txtTransl)
        continue

    if int(txtIn) == 4:
        t.printAll()

    if int(txtIn) == 5:
        break
