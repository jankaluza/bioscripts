import os
import sys

if int(sys.argv[1][:-4][sys.argv[1][:-4].rfind("_") + 1:]) <= int(9):
	os.system("mkdir -p 'less than 10'")
	os.system("cp " + sys.argv[1] + " 'less than 10'")
	sys.exit(0)

IDENTITY = -1
SINGLE_MISMATCH_IN_PRIMER = 0
MULTIPLE_MISMATCH_IN_PRIMER = 1
INSERTION = 3
DELETION = 4
INSERTIONS = 5
DELETIONS = 6
SINGLE_MISMATCH = 7
MULTIPLE_MISMATCH = 8
INSERTION_DELETION = 9
NONE = 255

state = NONE

LENGTH = 0

def change_state(nstate):
	global state
	if nstate < state:
		state = nstate

f = open(sys.argv[1], "r")

class Subject:
	def __init__(self, name):
		self.name = name
		self.identities = -1
		self.gaps = -1
		self.blast = []
		self.finished_id = 0
		self.start = 0
		self.end = 0

	def mismatches_in_range(self, mismatches, x, y):
		for mismatch in mismatches:
			if mismatch >= x and mismatch <= y:
				return False
		return True

	def is_novel(self):
		# find errors in homopolymers
		for i in range(len(self.blast)):
			b = self.blast[i]
			if b[1] != "|":
				fr = i - 10 - 4
				if fr < 0:
					fr = 0
				to = i + 10 + 4
				if to > len(self.blast) - 1:
					to = len(self.blast) - 1
				prev = ""
				cnt = 0
				for x in range(fr, to):
					if prev == self.blast[x][0]:
						cnt += 1
					else:
						cnt = 0
					prev = self.blast[x][0]
					if cnt == 4:
						return False

		# check if this sequence is in other individual too
		#if os.system("grep " + sys.argv[1][:-4] + " ../../pairs.txt") != 0:
			#return False
		return True

	def do(self):
		# simulate invalid data in the beginning
		while self.start != 1:
			self.blast.insert(0,['a', ' ', 't'])
			self.start -= 1
		while self.end != LENGTH:
			self.blast.append(['a', ' ', 't'])
			self.end += 1

		global state

		num_changes = 0

		if self.identities != LENGTH or self.gaps != 0:
			#print self.name
			#print self.gaps
			if self.gaps == 0:
				# check where the mismatch is
				mismatches = []
				for i in range(len(self.blast)):
					b = self.blast[i]
					if b[1] != "|":
						mismatches.append(i)

				# Mismatch is in the beginning or end of primer
				if len(mismatches) == 0 or self.mismatches_in_range(mismatches, 17, LENGTH-19):
					if self.identities == LENGTH - 1:
						change_state(SINGLE_MISMATCH_IN_PRIMER)
						print "single mismatch in primer"
					else:
						change_state(MULTIPLE_MISMATCH_IN_PRIMER)
						print "multiple mismatch in primer"
				else:
					if self.identities == LENGTH - 1:
						change_state(SINGLE_MISMATCH)
						print "single mismatch"
					else:
						change_state(MULTIPLE_MISMATCH)
						print "multiple mismatch"
				num_changes = len(mismatches)
			else:
				insertions = []
				deletions = []
				for i in range(len(self.blast)):
					b = self.blast[i]
					if b[1] != "|":
						if b[0] == '-':
							deletions.append(i)
						if b[2] == '-':
							insertions.append(i)

				mismatches = []
				for i in range(len(self.blast)):
					b = self.blast[i]
					if b[1] != "|" and not i in deletions and not i in insertions:
						mismatches.append(i)

				if (len(insertions) != 0 and len(deletions) != 0) or (len(mismatches) != 0 and len(insertions) != 0) or (len(mismatches) != 0 and len(deletions) != 0):
					print "insertions and deletions"
					change_state(INSERTION_DELETION)
				else:
					if len(insertions) != 0:
						if len(insertions) == 1:
							print "insertion"
							change_state(INSERTION)
						else:
							print "insertions"
							change_state(INSERTIONS)
					if len(deletions) != 0:
						if len(deletions) == 1:
							print "deletion"
							change_state(DELETION)
						else:
							print "deletions"
							change_state(DELETIONS)
				num_changes = len(insertions) + len(deletions)
		elif self.gaps == 0:
			print "identity"
			state = IDENTITY
			

		if state != NONE:
			if state == IDENTITY:
				os.system("mv " + sys.argv[1] + " ../found")
			elif state == SINGLE_MISMATCH_IN_PRIMER or state == MULTIPLE_MISMATCH_IN_PRIMER:
				os.system("mkdir -p 'mistake of the primer'")
				os.system("cp " + sys.argv[1] + " 'mistake of the primer'")
			elif state == SINGLE_MISMATCH:
				os.system("mkdir -p 'single nucleotide substitutions'")
				os.system("cp " + sys.argv[1] + " 'single nucleotide substitutions'")
			elif state == MULTIPLE_MISMATCH:
				if num_changes < 3:
					os.system("mkdir -p 'multiple nucleotide substitutions'")
					os.system("cp " + sys.argv[1] + " 'multiple nucleotide substitutions'")
				elif self.is_novel():
					print "NOVEL"
					os.system("mkdir -p 'novel'")
					os.system("cp " + sys.argv[1] + " 'novel'")
			elif state == INSERTION:
				os.system("mkdir -p 'single insertions'")
				os.system("cp " + sys.argv[1] + " 'single insertions'")
			elif state == INSERTIONS:
				if num_changes < 3:
					os.system("mkdir -p 'multiple insertions'")
					os.system("cp " + sys.argv[1] + " 'multiple insertions'")
				elif self.is_novel():
					print "NOVEL"
					os.system("mkdir -p 'novel'")
					os.system("cp " + sys.argv[1] + " 'novel'")
			elif state == DELETION:
				os.system("mkdir -p 'single deletions'")
				os.system("cp " + sys.argv[1] + " 'single deletions'")
			elif state == DELETIONS:
				if num_changes < 3:
					os.system("mkdir -p 'multiple deletions'")
					os.system("cp " + sys.argv[1] + " 'multiple deletions'")
				elif self.is_novel():
					print "NOVEL"
					os.system("mkdir -p 'novel'")
					os.system("cp " + sys.argv[1] + " 'novel'")
			elif state == INSERTION_DELETION:
				os.system("mkdir -p 'strange'")
				os.system("cp " + sys.argv[1] + " 'strange'")
			sys.exit(0)

subject = None
prev_query = False
indent = 0

for line in f.readlines():
	l = line
	if LENGTH == 0 and l.startswith("Length="):
		LENGTH=int(l[len("Length="):-1])

	l = line.lower()
		

	if l.startswith(">"):
		if subject:
			subject.do()
		if l.find("mulatta") != -1:
			subject = Subject(l)
		else:
			subject = None

	if subject:
		ind = l.find("identities = ");
		if ind != -1:
			if (len(subject.blast) != 0):
				subject.do()
				subject = Subject(subject.name)
			ind += len("identities = ")
			subject.identities = int(l[ind:ind + 3])
			print subject.name
			#LENGTH=int(l[ind+4:ind + 7])
			ind = l.find("gaps = ");
			ind += len("gaps = ")
			#print subject.name
			#print l[ind:ind+l[ind:].find("/")]
			subject.gaps = int(l[ind:ind+l[ind:].find("/")])

		if prev_query:
			prev_query = False
			l = l[indent:-1]
			i = 0
			for s in l:
				subject.blast[subject.finished_id + i].append(s)
				i += 1

		if l.startswith("query"):
			seq = l.split(" ")
			if subject.start == 0:
				subject.start = int(seq[2])
			while (len(seq[0]) == 0 or not seq[0][0] in ['a', 't', 'g', 'c']):
				del seq[0]

			subject.end = int(seq[2])

			seq = seq[0]
			indent = l.find(seq)
			for b in seq:
				subject.blast.append([b])
			prev_query = True

		if l.startswith("sbjct"):
			seq = l.split(" ")
			while (len(seq[0]) == 0 or not seq[0][0] in ['a', 't', 'g', 'c']):
				del seq[0]

			seq = seq[0]
			i = 0
			for b in seq:
				subject.blast[subject.finished_id + i].append(b)
				i += 1
			subject.finished_id += i

print "FINAL STATE IS", state

f.close()
