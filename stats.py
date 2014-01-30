# -*- coding: iso-8859-2 -*-
import os,sys

dirs = ["1_1_result", "1_2_result", "1_3_result", "1_4_result", "2_1_result", "2_2_result", "2_3_result", "2_4_result", "3_1_result", "3_2_result", "3_3_result", "3_4_result", "4_1_result", "4_2_result", "4_3_result"]

def count_in_dir(d, less = 0):
	i = 0
	i_reads = 0
	if not os.path.exists(d):
		return i, i_reads
	for y in os.listdir(d):
		x = d + "/" + y
		if x.find("_") == -1:
			continue
		if less:
			if int(x[x.rfind("_") + 1:]) < less:
				continue
		i += 1
		if x.endswith(".txt"):
			x = x[:-4]
		i_reads += int(x[x.rfind("_") + 1:])
		#fp = open(x, "r")
		#for l in fp.readlines():
			#if l.startswith(">"):
				#i_reads += 1
		#fp.close()
	return i, i_reads

for d in dirs:
	os.chdir(d)
	print d
	f = "statistika.xls"
	os.system("echo '<table>' > " + f)

	i, i_reads = count_in_dir("./")
	os.system("echo '<tr>' >> " + f)
	os.system("echo '<td>Celkově čtení</td>' >>" + f)
	os.system("echo '<td>' >>" + f)
	os.system("echo '" + str(i_reads) + "' >>" + f) 
	os.system("echo '</td>' >>" + f)
	os.system("echo '</tr>' >> " + f)

	os.system("echo '<tr>' >> " + f)
	os.system("echo '<td>Počet sekvencí po seskupení</td>' >>" + f)
	os.system("echo '<td>' >>" + f)
	os.system("ls|grep __|wc -l >>" + f) 
	os.system("echo '</td>' >>" + f)
	os.system("echo '</tr>' >> " + f)

	i, i_reads = count_in_dir("./", 5)

	os.system("echo '<tr>' >> " + f)
	os.system("echo '<td>Počet sekvencí čtených více nebo rovno 5x</td>' >>" + f)
	os.system("echo '<td>' >>" + f)
	os.system("echo '" + str(i) + "' >>" + f) 
	os.system("echo '</td>' >>" + f)
	os.system("echo '</tr>' >> " + f)

	os.system("echo '<tr>' >> " + f)
	os.system("echo '<td>Počet čtení v sekvencích čtených více nebo rovno 5x</td>' >>" + f)
	os.system("echo '<td>' >>" + f)
	os.system("echo '" + str(i_reads) + "' >>" + f) 
	os.system("echo '</td>' >>" + f)
	os.system("echo '</tr>' >> " + f)

	os.system("echo '<tr>' >> " + f)
	os.system("echo '<td>Počet identifikovaných MHC</td>' >>" + f)
	os.system("echo '<td>' >>" + f)
	os.system("ls found|grep .txt|wc -l >>" + f) 
	os.system("echo '</td>' >>" + f)
	os.system("echo '</tr>' >> " + f)

	os.system("echo '<tr>' >> " + f)
	os.system("echo '<td>Počet neidentifikovaných MHC</td>' >>" + f)
	os.system("echo '<td>' >>" + f)
	os.system("ls new|grep .txt|wc -l >>" + f) 
	os.system("echo '</td>' >>" + f)
	os.system("echo '</tr>' >> " + f)

	i, i_reads = count_in_dir("./new/less than 10")
	os.system("echo '<tr>' >> " + f)
	os.system("echo '<td>less then 10x počet sekvencí</td>' >>" + f)
	os.system("echo '<td>' >>" + f)
	os.system("echo '" + str(i) + "' >>" + f) 
	os.system("echo '</td>' >>" + f)
	os.system("echo '</tr>' >> " + f)
	os.system("echo '<tr>' >> " + f)
	os.system("echo '<td>less then 10x počet čtení v sekvencích</td>' >>" + f)
	os.system("echo '<td>' >>" + f)
	os.system("echo '" + str(i_reads) + "' >>" + f) 
	os.system("echo '</td>' >>" + f)
	os.system("echo '</tr>' >> " + f)

	i, i_reads = count_in_dir("./new/single nucleotide substitutions")
	os.system("echo '<tr>' >> " + f)
	os.system("echo '<td>single nucleotide substitutions počet sekvencí</td>' >>" + f)
	os.system("echo '<td>' >>" + f)
	os.system("echo '" + str(i) + "' >>" + f) 
	os.system("echo '</td>' >>" + f)
	os.system("echo '</tr>' >> " + f)
	os.system("echo '<tr>' >> " + f)
	os.system("echo '<td>single nucleotide substitutions počet čtení v sekvencích</td>' >>" + f)
	os.system("echo '<td>' >>" + f)
	os.system("echo '" + str(i_reads) + "' >>" + f) 
	os.system("echo '</td>' >>" + f)
	os.system("echo '</tr>' >> " + f)

	i, i_reads = count_in_dir("./new/single insertions")
	os.system("echo '<tr>' >> " + f)
	os.system("echo '<td>single nucleotide insertions počet sekvencí</td>' >>" + f)
	os.system("echo '<td>' >>" + f)
	os.system("echo '" + str(i) + "' >>" + f) 
	os.system("echo '</td>' >>" + f)
	os.system("echo '</tr>' >> " + f)
	os.system("echo '<tr>' >> " + f)
	os.system("echo '<td>single nucleotide insertions počet čtení v sekvencích</td>' >>" + f)
	os.system("echo '<td>' >>" + f)
	os.system("echo '" + str(i_reads) + "' >>" + f) 
	os.system("echo '</td>' >>" + f)
	os.system("echo '</tr>' >> " + f)

	i, i_reads = count_in_dir("./new/multiple insertions")
	os.system("echo '<tr>' >> " + f)
	os.system("echo '<td>multiple insertions počet sekvencí</td>' >>" + f)
	os.system("echo '<td>' >>" + f)
	os.system("echo '" + str(i) + "' >>" + f) 
	os.system("echo '</td>' >>" + f)
	os.system("echo '</tr>' >> " + f)
	os.system("echo '<tr>' >> " + f)
	os.system("echo '<td>multiple insertions počet čtení v sekvencích</td>' >>" + f)
	os.system("echo '<td>' >>" + f)
	os.system("echo '" + str(i_reads) + "' >>" + f) 
	os.system("echo '</td>' >>" + f)
	os.system("echo '</tr>' >> " + f)

	i, i_reads = count_in_dir("./new/single deletions")
	os.system("echo '<tr>' >> " + f)
	os.system("echo '<td>single nucleotide deletions počet sekvencí</td>' >>" + f)
	os.system("echo '<td>' >>" + f)
	os.system("echo '" + str(i) + "' >>" + f) 
	os.system("echo '</td>' >>" + f)
	os.system("echo '</tr>' >> " + f)
	os.system("echo '<tr>' >> " + f)
	os.system("echo '<td>single nucleotide deletions počet čtení v sekvencích</td>' >>" + f)
	os.system("echo '<td>' >>" + f)
	os.system("echo '" + str(i_reads) + "' >>" + f) 
	os.system("echo '</td>' >>" + f)
	os.system("echo '</tr>' >> " + f)

	i, i_reads = count_in_dir("./new/multiple nucleotide substitutions")
	os.system("echo '<tr>' >> " + f)
	os.system("echo '<td>multiple nucleotide substitutions počet sekvencí</td>' >>" + f)
	os.system("echo '<td>' >>" + f)
	os.system("echo '" + str(i) + "' >>" + f) 
	os.system("echo '</td>' >>" + f)
	os.system("echo '</tr>' >> " + f)
	os.system("echo '<tr>' >> " + f)
	os.system("echo '<td>multiple nucleotide substitutions počet čtení v sekvencích</td>' >>" + f)
	os.system("echo '<td>' >>" + f)
	os.system("echo '" + str(i_reads) + "' >>" + f) 
	os.system("echo '</td>' >>" + f)
	os.system("echo '</tr>' >> " + f)

	i, i_reads = count_in_dir("./new/mistake of the primer")
	os.system("echo '<tr>' >> " + f)
	os.system("echo '<td>mistakes in primers počet sekvencí</td>' >>" + f)
	os.system("echo '<td>' >>" + f)
	os.system("echo '" + str(i) + "' >>" + f) 
	os.system("echo '</td>' >>" + f)
	os.system("echo '</tr>' >> " + f)
	os.system("echo '<tr>' >> " + f)
	os.system("echo '<td>mistakes in primers počet sekvencí počet čtení v sekvencích</td>' >>" + f)
	os.system("echo '<td>' >>" + f)
	os.system("echo '" + str(i_reads) + "' >>" + f) 
	os.system("echo '</td>' >>" + f)
	os.system("echo '</tr>' >> " + f)

	i, i_reads = count_in_dir("./new/strange")
	os.system("echo '<tr>' >> " + f)
	os.system("echo '<td>strange počet sekvencí</td>' >>" + f)
	os.system("echo '<td>' >>" + f)
	os.system("echo '" + str(i) + "' >>" + f) 
	os.system("echo '</td>' >>" + f)
	os.system("echo '</tr>' >> " + f)
	os.system("echo '<tr>' >> " + f)
	os.system("echo '<td>strange počet čtení v sekvencích</td>' >>" + f)
	os.system("echo '<td>' >>" + f)
	os.system("echo '" + str(i_reads) + "' >>" + f) 
	os.system("echo '</td>' >>" + f)
	os.system("echo '</tr>' >> " + f)

	i, i_reads = count_in_dir("./new")
	os.system("echo '<tr>' >> " + f)
	os.system("echo '<td>součet chybových čtení</td>' >>" + f)
	os.system("echo '<td>' >>" + f)
	os.system("echo '" + str(i_reads) + "' >>" + f) 
	os.system("echo '</td>' >>" + f)
	os.system("echo '</tr>' >> " + f)

	i, i_reads = count_in_dir("./found")
	os.system("echo '<tr>' >> " + f)
	os.system("echo '<td>součet dobrých čtení</td>' >>" + f)
	os.system("echo '<td>' >>" + f)
	os.system("echo '" + str(i_reads) + "' >>" + f) 
	os.system("echo '</td>' >>" + f)
	os.system("echo '</tr>' >> " + f)

	os.system("echo '</table>' >> " + f)

	os.chdir("..")