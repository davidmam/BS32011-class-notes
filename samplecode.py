#this works but looks hidous! need to write a loop
cutsite=5 #cut-off for sequences

sequences={'species1':'-----AGCTTAC-ACG', 'species2':'GGGGGAGCTTAC----', 'species3':'G--A-AGCTTAC----'}
sequences['species1']=sequences['species1'][cutsite:]+sequences['species1'][:cutsite]
sequences['species2']=sequences['species2'][cutsite:]+sequences['species2'][:cutsite]
sequences['species3']=sequences['species3'][cutsite:]+sequences['species3'][:cutsite]


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

    
