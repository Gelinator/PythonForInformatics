count = 0
num = list()

while True:
    chif = raw_input("Enter a number:")
    if chif == "done" or chif == "Done":
        break
    else:
        try:
            num.append(float(chif))
            count += 1
        except:
            print "Enter a fucking number you dickwag"

print "Sum of all numbers:",sum(num)
print "Total number of instances:",count
print "Maximum:",max(num)
print "Minimum:",min(num)
