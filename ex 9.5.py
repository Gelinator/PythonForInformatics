while True:
    fh = raw_input("Enter file name :")
    try:
        text = open(fh)
        emailer = dict()
    
        for line in text:
            if line.startswith("From "):
                splitted = line.split()
                email = splitted[1].split("@")
                emailer[email[1]] = emailer.get(email[1],0) + 1
        print emailer
        break
    except:
            print "Enter a valid file name or make sure the source \nfile is in the same folder as program."


