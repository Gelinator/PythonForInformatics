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
                zeliste.append(wotwot[1])
        for words in zeliste:
            worder[words] = worder.get(words,0)+1
        count = None
        name = None
        for a,b in worder.items():
            if count is None or b > count:
                count = b
                name = a
        print name,count
        break
    except:
            print "Enter a valid file name or make sure the source \nfile is in the same folder as program."

