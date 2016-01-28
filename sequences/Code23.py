# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 08:36:04 2016

@author: Anonymax
"""

#set the working directory
#open the .fasta file for raw alignment
fh=open("raw_data.fasta",'r')

sequences=[]  
for line in fh.readlines():
    #for a line starting fromm '>'
	if line[0]=='>':
        name=line[1:].replace("\n",'')
        entry={'Species':name, 'sequence':''}
        sequences.append(entry)
    else:
        entry['sequence']= entry['sequence']+line.replace('\n','')
fh.close()

#setting the cut-off for sequences, start position for the first common unit
cutsite= 

for seq in sequences:
    seq['sequence'][:cutsite] #looking at the seq in 'seq' key and reading it from [:cutsite]
    seq['sequence']=seq['sequence'][cutsite:]+seq['sequence'][:cutsite] #rearranging the sequences
print(sequences)

    # making a new file to hold the output
output=open("sequences.fasta", "w")
    # writing the header and sequence 
output.write('>' + entry['Species'] + '\n' + entry['sequence'] + '\n')

for line in output.readlines():
    