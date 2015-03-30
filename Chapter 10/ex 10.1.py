while True:
    worder = dict()
    zeliste = list()
    wotwot = list()
    pouet = list()
    f = raw_input("Enter the file name: ")
    try:
        text = open(f)
        for lines in text:
            if lines.startswith("From "):
                wotwot = lines.split()
                zeliste.append(wotwot[1])
        for words in zeliste:
            worder[words] = worder.get(words,0)+1
        break
    except:
            print "Enter a valid file name or make sure the source \nfile is in the same folder as program."

for k,v in worder.items():
    pouet.append((v,k))
pouet.sort(reverse=True)

for v,k in pouet[:1]:
    print k,v
