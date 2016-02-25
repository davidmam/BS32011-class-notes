#defining a general function with arg: sitefile in .restrict, seqfile in .fasta
def getsites(sitefile,seqfile):

    fh=open(sitefile,'r')
    headers=[]
    sites=[]
    
    #processing the data
    for line in fh.readlines():
    	#for lines that do not startwith '#'...
        if not line.startswith('#'):
            if headers:
    			#strip empty space and split values for valid headers
                values=line.strip().split()
                #creating dictionaries for valid values
                if values:
                    new_data=zip(headers,values)
                    new_dict=dict(new_data)
                    #creating dicitionaries of integer values for selected headers
                    for h in ['Start','End','3prime','5prime']:
                        new_dict[h]=int(new_dict[h])
    			#adding new dictionary to sites list
                    sites.append(new_dict)
            else:
    		#for line starting with space, finding first valid header
                if line.replace(' ','').startswith('Start'):
                    headers=line.strip().split()
    
    fh=open(seqfile,'r')
    #reading sequence as one line by replacing line breaks with nothing
    seq=''.join(fh.readlines()[1:]).replace('\n','')
    gaps=0 #gaps count starts at 0
    esites={}
    for e in sites:
        #calculating and defining new start sites, keeping a tally of gaps as it goes through the sequnece
        while len(seq[:e['Start'] + gaps].replace('-','')) < e['Start']:
            gaps +=e['Start'] - len(seq[:e['Start'] + gaps].replace('-','')) 
        e['gappedstart']=e['Start']+gaps 
        try:
            esites[e['Enzyme_name']].append(e)
        except:
            esites[e['Enzyme_name']]=[e]
    fh.close()
    # add a fake 'last site' so the matching doesn't break
    sites.append({'Start': len(seq), 'End':len(seq), 
                  '3prime':len(seq),'5prime':len(seq),
                    'Restriction_site':'END', 'gappedstart':len(seq),
                    'Enzyme_name':'END'})
    for e in esites:
        esites[e].append({'Start': len(seq), 'End':len(seq), 
                  '3prime':len(seq),'5prime':len(seq),
                    'Restriction_site':'END', 'gappedstart':len(seq),
                    'Enzyme_name':'END'})
        
    return esites
