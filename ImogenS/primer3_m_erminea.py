primer3params={'Sequence_ID': 'm_erminea', 
               'Sequence_Included_Region': '4438,13338',
               'SEQUENCE_TARGET': '12000,50',
               'PRIMER_PRODUCT_SIZE_RANGE':'400-800',
               'PRIMER_MAX_TM': '61',
               'PRIMER_MIN_TM': '59'} #dictionary created to store parameters for selecting primers

# get the sequence for the species from folder
sequencefile='../ImogenS/m_erminea.fasta'

#opens and reads file. replaces carriage returns and dashes with nothing
primer3params['SEQUENCE_TEMPLATE']=''.join(open(sequencefile).readlines()[1:]).replace('\n','').replace('-','') 


p3i=open('primer3input_m_erminea.txt','w') #opens output file and prepares to write to it 

for k in primer3params.keys():
    p3i.write('%s=%s'%(k,primer3params[k] + '\n')) # outputs primer parameters in dictionary along with the full sequence for m_erminea in a format primer3 can read

p3i.close()