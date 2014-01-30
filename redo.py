import os,sys

dirs = ["1_1_result", "1_2_result", "1_3_result", "1_4_result", "2_1_result", "2_2_result", "2_3_result", "2_4_result", "3_1_result", "3_2_result", "3_3_result", "3_4_result", "4_1_result", "4_2_result", "4_3_result"]

for d in dirs:
	for t in os.listdir(d + "/new/"):
		if os.path.exists(d + "/new/" + t) and os.path.isdir(d + "/new/" + t):
			print d + "/new/" + t
			os.system("rm -rf '" + d + "/new/" + t + "'")

	os.system("cd " + d + "/new/; for i in *.txt; do python ../../parse.py $i; done; cd ../..")
