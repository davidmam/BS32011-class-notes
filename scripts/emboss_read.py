# Look up what the break command does, or use pass and an if/else loop.
# For the headers you know that the line will start with spaces then a certain word so look for that (the first valid line). 
# If the headers array is filled (ie if headers: ) then you can split the line into the data structure.
# Start with identifying the lines you want to throw away and the lines you want to keep.


fh=open("e_europaeus.restrict",'r')
headers=[]
sites=[]

#process the data
for line in fh.readlines():
	#read valid lines for lines not starting from '#'
    if not line.startswith('#'):
        if headers:
			#strip and split values for valid headers
            values=line.strip().split()
            new_data=zip(headers,values)
            new_dict=dict(new_data)
            new_dict['sites'['Start']] = int(new_dict'sites'['Start'])
			#append new dictionary to sites
            sites.append(new_dict)
        else:
		#for line starting with space, find first valid header
            if line.replace(' ','').startswith('Start'):
                headers=line.strip().split()

#calculate and define new start sites
seq=fh.readlines("e_europaeus.fasta") #sequence with gaps read from dictionary
gaps=0
for line in fh.readlines():
    len(seq[:'Start' + gaps]).replace('-','')
for e in 'Restriction_site':
    while len(seq[:'Start'] + gaps).replace('-',''):
        gaps += len - e['Start']
        e['gappedstart']=e['Start']+gaps 

fh.close()