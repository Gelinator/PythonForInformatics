num = 0
count = 0
total = 0
average = 0


while True:
    num = raw_input("Enter a number:")
    if num == "done":
        break
    else:
        try:
            count += 1
            total += int(num)
            average = total/float(count)
        except:
            print "Invalid input"
print count
print total
print average
