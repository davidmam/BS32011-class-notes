#open the .fasta file for raw alignment
fh=open("raw_data.fasta",'r')

sequences=[]  
for line in fh.readlines():
    #for a line starting from '>'
    if line[0]=='>':
        name=line[1:].replace("\n",'')
        entry={'Species':name, 'sequence':''}
        sequences.append(entry)
    else:
        entry['sequence']= entry['sequence']+line.replace('\n','')
fh.close()

#setting the cut-off for sequences, start position for the first common unit
cutsite= 662

output=open("sequences.fasta", "w")
for seq in sequences:
    seq['sequence'][:cutsite] #looking at the seq in 'seq' key and reading it from [:cutsite]
    seq['sequence']=seq['sequence'][cutsite:]+seq['sequence'][:cutsite] #rearranging the sequences
    output.write('>' + seq['Species'] + '\n' + seq['sequence'] + '\n') #write output within the loop to go through the whole list of dictionaries
print(sequences)

output.close()