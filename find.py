import os
import sys
from StringMatcher import *
import pprint
import bisect

def reverse_complement(s):
	complements = {'A':'T', 'C':'G', 'T':'A', 'G':'C', 'N':'N'}
	
	sc = reversed(s)
	sc = [complements[c] for c in sc]

	return ''.join(sc)

matched = []
pairs = {}

f = open(sys.argv[1])
lines = f.readlines()

def get_seq_count():
	global lines
	count = 0
	for line in lines:
		if line.startswith(">"):
			count += 1
	return count

def get_seq(i):
	global lines
	data = ""
	header = ""
	for line in lines:
		if line.startswith(">"):
			if i == 0:
				return (header, data)
			i = i - 1
			header = line[:-1]
		else:
			data = line[10:-11] # remove MIDs and \n

seq_count = get_seq_count()
sm = StringMatcher()

def index(a, x):
	i = bisect.bisect_left(a, x)
	if i != len(a) and a[i] == x:
		return True
	return False

os.system("mkdir " + sys.argv[1] + "_result")

for i in range(seq_count):
	if index(matched, i + 1):
		continue
	header, data = get_seq(i + 1)
	pairs[i + 1] = []

	output = ""

	print i + 1, "/", seq_count, "( matched =",len(matched), ")"
	d = ""
	h = ""
	ind = 0
	for line in lines:
		if line.startswith(">"):
			ind = ind + 1
			h = line[:-1]
		else:
			d = line[10:-11]
			d_r = reverse_complement(d)
			if index(matched, ind):
				continue
			sm.set_seqs(data, d)
			found = sm.distance() <= int(sys.argv[2])
			sm.set_seqs(data, d_r)
			found = found or sm.distance() <= int(sys.argv[2])
			if found:
				pairs[i + 1].append(ind)
				matched.append(ind)
				matched.sort()
				output += h + "\n" + d + "\n"

	if not index(matched, i + 1):
		matched.append(i + 1)
		matched.sort()

	f = open(sys.argv[1] + "_result/" + str(i + 1) + (8 - len(str(i + 1))) * "_" + str(len(pairs[i + 1])), "w")
	f.write(output);
	f.close()

#pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(pairs)
