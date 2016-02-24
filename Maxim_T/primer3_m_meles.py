primer3params={'Sequence_ID': 'm_meles', 
               'Sequence_Included_Region': '4438,13338',
               'SEQUENCE_TARGET': '8000,50',
               'PRIMER_PRODUCT_SIZE_RANGE':'100-300',
               'PRIMER_MAX_TM': '61',
               'PRIMER_MIN_TM': '59'}

# get the sequence
sequencefile='m_meles.fasta'

primer3params['SEQUENCE']=''.join(open(sequencefile).readlines()[1:]).replace('\n','').replace('-','')

#sequence_target is start site +/- a space around it. 50bp?

p3i=open('primer3input_m_meles.txt','w')

for k in primer3params.keys():
    p3i.write('%s=%s'%(k,primer3params[k] + '\n'))

p3i.close()