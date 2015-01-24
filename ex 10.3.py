count = 0
freq = dict()
pouet = list()
wiii = list()
blah = list()
alphabet = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
while True:
    fhandle = raw_input("Enter file name: ")
    text = open(fhandle)
    for line in text:
        wiii = line.strip()
        for letters in wiii:
            letters = letters.lower()
            if letters not in alphabet:
                pass
            else:
                if letters not in freq:
                    freq[letters] = 1
                else:
                    freq[letters] += 1
    break
for k,v in freq.items():
    pouet.append((v,k))
pouet.sort(reverse=True)

for v,k in pouet:
    print k,v
