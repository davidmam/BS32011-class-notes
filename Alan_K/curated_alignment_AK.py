#open the .fasta file for raw alignment
fh=open("raw_data.fasta",'r')

sequences=[]  #created an empty list named sequences
for line in fh.readlines():
    #read lines starting with '>' and replace new lines with nothing to create a single line
    if line[0]=='>':
        name=line[1:].replace("\n",'')
        entry={'Species':name, 'sequence':''} #dictionary created containing 'species' and 'sequence' before adding these to sequence list
        sequences.append(entry) 
    else:
        entry['sequence']= entry['sequence']+line.replace('\n','')
fh.close()

#setting the cut-off for sequences, start position for the first common unit
cutsite= 

output=open("sequences.fasta", "w")
for seq in sequences:
    seq['sequence'][:cutsite] #looking at the seq in 'seq' key and reading it from [:cutsite]
    seq['sequence']=seq['sequence'][cutsite:]+seq['sequence'][:cutsite] #rearranging the sequences by putting the sequence before cutsite at the end
    output.write('>' + seq['Species'] + '\n' + seq['sequence'] + '\n') #write output within the loop to go through the whole list of dictionaries
print(sequences)

output.close()
