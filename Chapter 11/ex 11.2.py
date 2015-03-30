import re
count = 0
total = 0
fh = raw_input("Enter a file name : ")

text = open(fh)

for line in text:
	line = line.strip()
	x = re.findall('^New Revision:.([0-9]+)',line)
	if line.startswith("New Revision:"):
		count += 1
	for i in x:
		i = float(i)
		total += i
		
print total/count
		
