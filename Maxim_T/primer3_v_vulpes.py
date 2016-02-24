primer3params={'Sequence_ID': 'v_vulpes', 
               'SEQUENCE_INCLUDED_REGION': '4438,13338',
               'SEQUENCE_TARGET': '8000,50',
               'PRIMER_PRODUCT_SIZE_RANGE':'400-800',
               'PRIMER_MAX_TM': '61',
               'PRIMER_MIN_TM': '58'}

# get the sequence
sequencefile='v_vulpes.fasta'

primer3params['SEQUENCE_TEMPLATE']=''.join(open(sequencefile).readlines()[1:]).replace('\n','').replace('-','')

#sequence_target is start site +/- a space around it. 50bp?

p3i=open('primer3input_v_vulpes.txt','w')

for k in primer3params.keys():
    p3i.write('%s=%s'%(k,primer3params[k] + '\n'))

p3i.close()