primer3params={'Sequence_ID': 'm_meles', 
               'SEQUENCE_INCLUDED_REGION': '4438,10338',
               'SEQUENCE_TARGET': '6800,100',
               'PRIMER_PRODUCT_SIZE_RANGE':'400-800',
               'PRIMER_MAX_TM': '61',
               'PRIMER_MIN_TM': '58'}

# get the sequence
sequencefile='m_meles.fasta'

primer3params['SEQUENCE_TEMPLATE']=''.join(open(sequencefile).readlines()[1:]).replace('\n','').replace('-','')

#sequence_target is start site +/- a space around it. 50bp?

p3i=open('primer3input_m_meles.txt','w')

for k in primer3params.keys():
    p3i.write('%s=%s'%(k,primer3params[k] + '\n'))

p3i.close()