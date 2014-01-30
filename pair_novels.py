# -*- coding: iso-8859-2 -*-
import os,sys

dirs = ["1_1_result", "1_2_result", "1_3_result", "1_4_result", "2_1_result", "2_2_result", "2_3_result", "2_4_result", "3_1_result", "3_2_result", "3_3_result", "3_4_result", "4_1_result", "4_2_result", "4_3_result"]

pairs = []
dds = []

def reverse_complement(s):
	complements = {'A':'T', 'C':'G', 'T':'A', 'G':'C', 'N':'N'}
	
	sc = reversed(s)
	sc = [complements[c] for c in sc]

	return ''.join(sc)

for d in dirs:
	print d

	if not os.path.exists(d + "/new/novel"):
		continue

	for x in os.listdir(d + "/new/novel"):
		if x.find("_") == -1:
			continue
		f = open(d + "/" + x[:-4], "r")
		f1 = f.readlines()[1][:-1]
		f1r = reverse_complement(f1)
		f.close()
		found2 = False
		for d2 in dirs:
			if not os.path.exists(d2 + "/new/novel"):
				continue

			for x2 in os.listdir(d2 + "/new/novel"):
				if x2.find("_") == -1 or d + "/" + x == d2 + "/" + x2:
					continue
				f = open(d2 + "/" + x2[:-4], "r")
				f2 = f.readlines()[1][:-1]
				f.close()
				if f1 == f2 or f1r == f2:
					found2 = True
					found = False
					for i in range(len(pairs)):
						if d + "/" + x[:-4] in pairs[i] and not d2 + "/" + x2[:-4] in pairs[i]:
							#print d + "/" + x, d2 + "/" + x2
							pairs[i].append(d2 + "/" + x2[:-4])
							found = True
							break
						elif d2 + "/" + x2[:-4] in pairs[i] and not d + "/" + x[:-4] in pairs[i]:
							#print d + "/" + x, d2 + "/" + x2
							pairs[i].append(d + "/" + x[:-4])
							found = True
							break
						elif d2 + "/" + x2[:-4] in pairs[i] and d + "/" + x[:-4] in pairs[i]:
							found = True
							break
					if not found:
						pairs.append([d + "/" + x[:-4], d2 + "/" + x2[:-4]])
						#print d + "/" + x, d2 + "/" + x2
		if found2 == False:
			pairs.append([d + "/" + x[:-4]])

for p in pairs:
	print '\t'.join(p)
