while True:
    f = raw_input("Enter the file name: ")
    count = 0
    try:
        
        text = open(f)
        for lines in text:
            if lines.startswith("From "):
                dawg = lines.split()
                count += 1
                print dawg[1]
        print "There were",count, "lines in the file with Form as the first word."
        break
    except:
            print "Enter a valid file name or make sure the source \nfile is in the same folder as program."

