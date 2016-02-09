# script generates data from EMBOSS .restrict output

#open the .restrict files
fh=open("*.restrict", 'r')
for line in fh.readlines():
	
	# skip invalid lines
	if line[0]=='#':
		#replace with nothing
		line=line[0:].replace('\n','')
		
		# create a dictionary
		data={}
		headers=line.strip().split() #creates keys
		values=lines.strip().split()
		entry=zip(headers, values)
		entry_dict= dict(entry)		

		# calculate start for gapped sequences
	for start in readlines.():
		len(seq[:n])==n #how to specify the start
		len(seq[:n]).replace('-', '')==n2 #how to specify new start
		# append to the list 
	data.append(entry_dict)

fh.close()

# for line in fh.readlines():
# 	#check line is valid data
# 	values=lines.strip().split()
# 	entry=zip(headers, values)
# 	entry_dict= dict(entry)
# 	data.append(entry_dict) 

#data.append(dict(zip(headers, line.strip().split())) is one combined line of the long way above
