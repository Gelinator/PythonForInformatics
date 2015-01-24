num = 0
count = 0
total = 0
average = 0
list = []


while True:
    num = raw_input("Enter a number:")
    if num == "done":
        break
    else:
        try:
            count += 1
            total += int(num)
            average = total/float(count)
            list.append(num)
        except:
            print "Invalid input"
            count -= 1
            continue

print total
print count
print average
print min(list)
print max(list)
