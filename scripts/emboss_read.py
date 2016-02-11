#defining a general function with arg: sitefile in .restrict, seqfile in .fasta
def getsites(sitefile,seqfile):

    fh=open(sitefile,'r')
    headers=[]
    sites=[]
    
    #processing the data
    for line in fh.readlines():
    	#reading valid lines for lines not starting from '#'
        if not line.startswith('#'):
            if headers:
    			#stripping and splitting values for valid headers
                values=line.strip().split()
                #creating dictionaries for valid values
                if values:
                    new_data=zip(headers,values)
                    new_dict=dict(new_data)
                    #creating dicitionaries of integer values for selected headers
                    for h in ['Start','End','3prime','5prime']:
                        new_dict[h]=int(new_dict[h])
    			#appending new dictionary to sites
                    sites.append(new_dict)
            else:
    		#for line starting with space, finding first valid header
                if line.replace(' ','').startswith('Start'):
                    headers=line.strip().split()
    
    fh=open(seqfile,'r')
    #reading sequence as one line
    seq=''.join(fh.readlines()[1:]).replace('\n','')
    gaps=0
    for e in sites:
        #calculating and defining new start sites
        while len(seq[:e['Start'] + gaps].replace('-','')) < e['Start']:
            gaps +=e['Start'] - len(seq[:e['Start'] + gaps].replace('-','')) 
        e['gappedstart']=e['Start']+gaps 
    fh.close()
    # add a fake 'last site' so the matching doesn't break
    sites.append({'Start': len(seq), 'End':len(seq), 
                  '3prime':len(seq),'5prime':len(seq),
                    'Restriction_site':'END', 'gappedstart':len(seq),
                    'Enzyme_name':'END'})
    return sites
