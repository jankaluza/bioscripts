import os
import sys

os.system("sed -n 2p " + sys.argv[1] + " > a")
os.system("sed -n 2p " + sys.argv[2] + " > b")

os.system("blastn -subject a -query b")
