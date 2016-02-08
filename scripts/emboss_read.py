# Look up what the break command does, or use pass and an if/else loop.
# For the headers you know that the line will start with spaces then a certain word so look for that (the first valid line). 
# If the headers array is filled (ie if headers: ) then you can split the line into the data structure.
# Start with identifying the lines you want to throw away and the lines you want to keep.

def getsites(sitefile,seqfile):

    fh=open(sitefile,'r')
    headers=[]
    sites=[]
    
    #process the data
    for line in fh.readlines():
    	#read valid lines for lines not starting from '#'
        if not line.startswith('#'):
            if headers:
    			#strip and split values for valid headers
                values=line.strip().split()
                if values:
                    new_data=zip(headers,values)
                    new_dict=dict(new_data)
                    for h in ['Start','End','3prime','5prime']:
                        new_dict[h]=int(new_dict[h])
    			#append new dictionary to sites
                    sites.append(new_dict)
            else:
    		#for line starting with space, find first valid header
                if line.replace(' ','').startswith('Start'):
                    headers=line.strip().split()
    
    #calculate and define new start sites
    fh=open(seqfile,'r')
    seq=''.join(fh.readlines()[1:]).replace('\n','') #sequence with gaps read from dictionary
    gaps=0
    for e in sites:
        while len(seq[:e['Start'] + gaps].replace('-','')) < e['Start']:
            gaps +=e['Start'] - len(seq[:e['Start'] + gaps].replace('-','')) 
        e['gappedstart']=e['Start']+gaps 
    fh.close()
    return sites