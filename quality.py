import os
import sys

from math import fsum
def average(x):
	return fsum(x)/float(len(x)) if x else 0

quality = []
is_reversed = []

first = ""
names = []
f = open(sys.argv[1])
for line in f.readlines():
	if line.startswith(">"):
		s = line.split(' ')
		name = s[0][1:]
		names.append(name)
	else:
		if len(first) == 0:
			first = line
			is_reversed.append(False)
		else:
			if first == line:
				is_reversed.append(False)
			else:
				is_reversed.append(True)
				print "X"
			
f.close()

cmd = "/opt/454/apps/gsSeqTools/bin/sffinfo -q " + sys.argv[2] + " " + " ".join(names) + " > quality"
print cmd
os.system(cmd)

data = ""
x = 0;
f = open("quality", "r")
for line in f.readlines():
	if line.startswith(">"):
		if len(data) != 0:
			s = data.split(" ")
			try:
				while True:
					s.remove('')
			except:
				pass
			if is_reversed[x]:
				s.reverse()
				print "reversing"
			if len(quality) == 0:
				for i in s:
					quality.append([int(i)])
			else:
				for i in range(len(quality)):
					quality[i].append(int(s[i]))
			data = ""
		x += 1
	else:
		data += line.replace("\n", " ")

#if len(data) != 0:
	#s = data.split(" ")
	#print s
first = "MIDMIDMIDD" + first[:-1] + "MIDMIDMIDD"
for i in range(len(quality)):
	quality[i] = average(quality[i])
	print i, first[i], quality[i]
#print quality

val, idx = min((val, idx) for (idx, val) in enumerate(quality))
print val, idx, len(quality), first[idx], len(first)

f.close()
