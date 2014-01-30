import os
import sys

files = sorted(os.listdir("."), key=os.path.getsize, reverse=True)
os.system("mkdir -p found")
os.system("mkdir -p new")

def seq_length(s):
	x = open(s)
	l = len(x.read()) - 1# - \n - len(mids)
	x.close()
	return l

def parse(r, length):
	acs = []
	x = open(r)
	tmp = ""
	skip = False
	for l in x.readlines():
		if l.startswith(">") and l.find("|") != -1:
			skip = False
			if l.lower().find("mulatta") == -1:
				skip = True
			tmp = l[l.find("|") + 1:l.rfind("|")]
		elif l.find("Identities") != -1 and l.find(length + "/" + length) != -1 and l.find("0/" + length) != -1:
			if not skip:
				acs.append(tmp)
	x.close()
	return acs

for f in files:
	if f.find("_") == -1:
		continue
	if int(f[f.rfind("_") + 1:]) < int(sys.argv[1]):
		continue
	if os.path.exists("found/" + f + ".txt") or os.path.exists("new/" + f + ".txt"):
		sys.stdout.write("Processing " + f + ": already done in previous run\n")
		continue
	os.system("sed -n 2p " + f + " > a")
	l = str(seq_length("a"))
	sys.stdout.write("Processing " + f + " (length = " + l + "): ")
	sys.stdout.flush()
	r = -1
	while r != 0:
		sys.stdout.write("... blasting ")
		sys.stdout.flush()
		r = os.system("blastn -remote -db nr -query a -max_target_seqs 25 > output 2>/dev/null") # 2>/dev/null

	acs = parse("output", l)
	#found = os.system("cat output|grep Identities|grep '(100%)'|grep '(0%)'|grep '" + l + "/" + l + "'|grep '0/" + l + "'")
	#if found == 0:
	if len(acs) != 0:
		print "FOUND in database:", acs
		os.system("cp output found/" + f + ".txt")
	else:
		print "NEW SEQUENCE"
		os.system("cp output new/" + f + ".txt")
	#sys.exit(0)


