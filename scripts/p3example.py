primer3params={'Sequence_ID': '', 
               'Sequence_Included_Region': '4438,13338',
               'SEQUENCE_TARGET': '',
               'PRIMER_PRODUCT_SIZE_RANGE':'100-300',
               'PRIMER_MAX_TM': '61',
               'PRIMER_MIN_TM': '59'}
               
# gethe sequence
sequencefile='s_vulgaris.fasta'

primer3params['SEQUENCE']=''.join(open(sequencefile).readlines()[1:]).replace('\n','')

#sequence_target is start site +/- a space around it. 50bp?

p3i=open('primer3input.txt','w')

for k in primer3params.keys():
    p3i.write('%s=%s'%(k,primer3params[k])) ##ther is something missing

p3i.close()


