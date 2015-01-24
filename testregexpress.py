import re
count = 0
hand = open('mbox-short.txt')
for line in hand:
    line = line.strip()
    if re.search("^From:.+@", line):
        print line
        count +=1


print 'There are',count,'instances'
