words = list()
wouerd = list()

while True:
    fhandle = raw_input("Enter a file name: ")
    text = open(fhandle)
    for line in text:
        words = line.split()
        for i in words:
            if i in wouerd:
                pass
            else:
                wouerd.append(i)
                wot = sorted(wouerd)
    break
print wot
