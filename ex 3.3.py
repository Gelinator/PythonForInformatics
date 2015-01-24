try:
    grade = float(raw_input("What is your score:"))
 
    
except:
    
    print "Bad score"
    quit()
if grade > 1.0:
    print "Bad score"
    
elif grade >= 0.9:
    print "A"
elif grade >= 0.8:
    print "B"
elif grade >= 0.7:
    print "C"
elif grade >= 0.6:
    print "D"
else:
    print "F"

