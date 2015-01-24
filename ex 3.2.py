try:
    hours = float(raw_input("How many hours:"))
    rate = float(raw_input("At what rate:"))
except:
    print "Please enter numbers."
    quit()
pay = 0

if hours > 40:
    pay = rate * (0.5 * (hours-40) + hours)

else:
    pay = rate * hours

print pay
