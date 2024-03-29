#Script to intersect .vcf with .BED file
#Author: Zarrine Raazi
#Version: 1.0.0
#09/05/2021

import pandas as pd
import argparse

VERSION = "VERSION: 1.0.0"
AUTHOR = "AUTHOR: Zarrine Raazi(zarrineraazi17@gmail.com)"
#outF = open("myOutFile.vcf", "w")
f = open("example.vcf", "r")
flist = f.readlines()
header=[]

for line in flist:
	if line.startswith("##") or line.startswith("#"):
		header.append(line)
myheader = "".join(map(str, header))	


# Create the parser
parser = argparse.ArgumentParser()
# Add an argument
#parser.add_argument("-a", help = "vcf file")
parser.add_argument('-a', help='Input vcf file to be read.')
parser.add_argument("-b", help = "Input bed file to be read.")
parser.add_argument("-o", help = "Print results in outfile.Give .vcf extension ")
# Parse the argument
args = parser.parse_args()

f1 = open(args.a)
f2 = open(args.b)
outF= open(args.o, 'w') 

outF.write(myheader)

#read .vcf file
data1 = pd.read_csv(f1, sep ='\t', skiprows = 22)
#print(data1)

#reading rows into list
dfrows = data1.to_numpy().tolist()

# converting column data to list
vchrom = data1["#CHROM"].tolist()
vpos = data1["POS"].tolist()

#read .BED file
data2 = pd.read_csv(f2, sep ='\t', header = None, usecols = [0,1,2])

# converting column data to list
bchrom = data2[0].tolist()
bstart = data2[1].tolist()
bend = data2[2].tolist()

print(VERSION)
print(AUTHOR)
rows = []
for i in range(len(vpos)):
	for j in range(len(bstart)):
		if ((vpos[i] >= bstart[j]) and (vpos[i]<= bend[j])):
			list_val = dfrows[i]
			myjoin = "\t".join(map(str, list_val))
			
			#print (myjoin)
			outF.write(myjoin+"\n") 
			
			#print (bchrom[j],"\t",bstart[j], "\t", bend[j], "\t", vchrom[i],"\t",vpos[i]) #To output as .bed file


			
			
			
			

