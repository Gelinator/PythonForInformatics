while True:
    f = raw_input("Enter the file name: ")
    try:
        text = open(f)
        domain_count = dict()
        for line in text:
            if line.startswith("From "):
                line_words = line.split()
                email = line_words[1].split('@')
                domain_count[email[1]] = domain_count.get(email[1], 0) + 1
        print domain_count
        break
        
    except:
            print "Enter a valid file name or make sure the source \nfile is in the same folder as program."

