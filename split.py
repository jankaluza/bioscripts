import os
import sys

data = ""
first = False
matched_first = False

f = open("mhc")
for line in f.readlines():
	if line.startswith(">"):
		if matched_first:
			if data.endswith(sys.argv[2]):
				print data
		data = line
		first = True
		matched_first = False
	elif first:
		if line.startswith(sys.argv[1]):
			matched_first = True
		data += line[:-1]
	else:
		data += line[:-1]
