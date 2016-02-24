#moderated by Simon Bajew on 23/02/2016

#setting up parameters for Primer3
primer3params={'Sequence_ID': 'l_europaeus', 
               'SEQUENCE_INCLUDED_REGION': '4438,10338',
               'SEQUENCE_TARGET': '5000,50',
               'PRIMER_PRODUCT_SIZE_RANGE':'400-800',
               'PRIMER_MAX_TM': '61',
               'PRIMER_MIN_TM': '58'}

#getting the sequence in FASTA file
sequencefile='C:/Users/SimonB/Desktop/BS32011-class-notes/sequences/individual/l_europaeus.fasta'

#replacing gaps in the sequence
primer3params['SEQUENCE_TARGET']=''.join(open(sequencefile).readlines()[1:]).replace('\n','').replace('-','')

#writing Primer3 output file
p3i=open('primer3_lepus.txt','w')
for k in primer3params.keys():
    p3i.write('%s=%s'%(k,primer3params[k] + '\n'))

p3i.close()