import re 

files = open("code2.py")
for line in files:
	line = line.rstrip()
	if re.search("> [0-9].*[0-9]", line):
		s = re.findall("> [0-9].*[0-9]", line)
		print s