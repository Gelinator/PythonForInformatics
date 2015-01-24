numbers = []

while True:
    num = raw_input("Enter a number: ")
    if num == 'done' or num == 'Done':
        break
    else:
        numbers.append(int(num))

print 'Maximum:',max(numbers)
print 'Minimum:',min(numbers)
