     #setting the cut-off for sequences  
cutsite= 5
    #creating a list of dictionaries with two pairs of key:value
sequences=[
{'name':'species1','seq':'-----AGCTTAC-ACG'},
{'name':'species2','seq':'GGGGGAGCTTAC----'},
{'name':'species3','seq':'G--A-AGCTTAC----'}]                                      

     #reassinging the sequences according to the cut-ff    
for seq in sequences:
    seq['seq'][:cutsite] #looks at the seq in 'seq' key and read it from :cutsite
    seq['seq']=seq['seq'][cutsite:]+seq['seq'][:cutsite] #rearranged the sequences
print(sequences)

    #setting the limit for viewing sequences  
limit=5
    # making a new file to hold the output
output=open("sequences.fasta", "w")
    # writing the header and sequence 
output.write('>' + seq['name'] + '\n' + seq['seq'] + '\n')



output.readline(limit)

if len(output)>5:
    output=output[:5]

def limiting(output):
    output=output[:5]
    return output
    
    for x in sequences:
    print(x['name'], x['seq'])
