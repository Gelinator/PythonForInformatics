import re
count = 0
fh = raw_input("Enter a file name : ")
regExp = raw_input("Enter a regular expression : ")

text = open(fh)

for line in text:
	line = line.strip()
	if re.search(regExp,line):
		count += 1

print fh, "had",count,"lines that matched",regExp
