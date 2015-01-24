while True:
    worder = dict()
    zeliste = list()
    wotwot = list()
    f = raw_input("Enter the file name: ")
    try:
        text = open(f)
        for lines in text:
            if lines.startswith("From "):
                wotwot = lines.split()
                zeliste.append(wotwot[2])
        for words in zeliste:
            worder[words] = worder.get(words,0)+1
        print worder
        break
    except:
            print "Enter a valid file name or make sure the source \nfile is in the same folder as program."

