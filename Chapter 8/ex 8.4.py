while True:
    f = raw_input("Enter the file name: ")
    dawg=[]
    try:
        text = open(f)
        for lines in text:
            if lines.startswith("From"):
                line = lines.split()
                for word in line:
                    dawg.append(word)
        print dawg
        break

    except:
        print "Enter a valid file name or make sure the source \nfile is in the same folder as program."

