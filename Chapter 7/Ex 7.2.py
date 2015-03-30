while True:
    f = raw_input("Enter the file name: ")
    try:
        mailbox = open(f)
        count = 0
        total = 0
        for line in mailbox:
            if line.startswith("X-DSPAM-Confidence:"):
                count +=1
                pos = line.find(":")
                total += float(line[pos + 1:])

        print total/count
        break
    except:
        print "Enter a valid file name or make sure the source \nfile is in the same folder as program."
