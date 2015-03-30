count = 0
day = dict()

while True:
    fhandle = raw_input("Enter file name: ")
    text = open(fhandle)
    for line in text:
        if line.startswith("From "):
            meh = line.split()
            blah = meh[1]
            if blah not in day:
                day[blah] = 1
            else:
                day[blah] += 1
    

    break
bigcount = None
bigword = None
for word,count in day.items():
    if bigcount == None or count > bigcount:
        bigword = word
        bigcount = count

print bigword, bigcount
