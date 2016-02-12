# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 10:54:36 2016

@author: O202B
"""

primer3params={'SEQUENCE_TARGET': '',
               'SEQUENCE':'',
               'PRIMER_PRODUCT_SIZE':'100-300',
               'PRIMER_TM_MAX': 61,
               'PRIMER_TM_MIN': 59
               }
               
# gethe sequence
sequencefile='f_silvestris.fasta'

primer3params['SEQUENCE']=''.join(open(sequencefile).readlines()[1:]).replace('\n','')

#sequence_target is start site +/- a space around it. 50bp?

p3i=open('primer3input.txt','w')

for k in primer3params.keys():
    p3i.write('%s=%s'%(k,primer3params[k])) ##ther is something missing

p3i.close()


