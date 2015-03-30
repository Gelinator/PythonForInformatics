count = 0
timeofday = dict()
wiii = list()

while True:
    fhandle = raw_input("Enter file name: ")
    text = open(fhandle)
    for line in text:
        if line.startswith("From "):
            meh = line.split()
            blah = meh[5]
            wot = blah.split(":")
            plotte = wot[0]
            wiii = sorted(plotte)
            if plotte not in timeofday:
                timeofday[plotte] = 1
            else:
                timeofday[plotte] += 1
    break
for key in sorted(timeofday):
    print "%s %s" % (key, timeofday[key])
