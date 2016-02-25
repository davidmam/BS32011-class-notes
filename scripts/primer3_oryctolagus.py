#moderated by Simon Bajew on 23/02/2016
#Primer3 parameters can be found at http://primer3.sourceforge.net/primer3_manual.htm

#setting up parameters for Primer3
primer3params={'Sequence_ID': 'o_cuniculus', 
               'SEQUENCE_INCLUDED_REGION': '5300,14000',
               'SEQUENCE_TARGET': '9300,150',
               'PRIMER_PRODUCT_SIZE_RANGE':'400-800',
               'PRIMER_MAX_TM': '61',
               'PRIMER_MIN_TM': '58'}

#getting the sequence in FASTA file
sequencefile='../sequences/individual/o_cuniculus.fasta'

#replacing gaps in the sequence
primer3params['SEQUENCE_TEMPLATE']=''.join(open(sequencefile).readlines()[1:]).replace('\n','').replace('-','')

#writing Primer3 input file
p3i=open('primer3_oryctolagus.txt','w')
for k in primer3params.keys():
    p3i.write('%s=%s'%(k,primer3params[k] + '\n'))

p3i.close()
