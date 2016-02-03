#Change the directory, change os.chdir to wherever file is on your computer
import os
os.getcwd
os.chdir('/Users/Alan/BS32011-class-notes/sequences/individual')

# script generates data from EMBOSS .restrict output
#open the .restrict files
fh=open("e_europaeus.restrict", 'r') #can't get wildcards ? and * to work yet so specific file must be opened
[n for n in fh.readlines() if not n.startswith('#')] #removes lines starting with a # (not quite sure how but it works)
		
		# create a dictionary
data={}
headers=line.strip().split() #creates keys
values=line.strip().split()
entry=zip(headers, values)
entry_dict= dict(entry)		

		# calculate start for gapped sequences
    #still being worked on, looking at breaks currently
for start in readlines.():
		len(seq[:n])==n #how to specify the start
		len(seq[:n]).replace('-', '')==n2 #how to specify new start
		# append to the list 
	data.append(entry_dict)

fh.close()

# for line in fh.readlines():
# 	#check line is valid data
# 	values=lines.strip().split()
# 	entry=zip(headers, values)
# 	entry_dict= dict(entry)
# 	data.append(entry_dict) 

#data.append(dict(zip(headers, line.strip().split())) is one combined line of the long way above
