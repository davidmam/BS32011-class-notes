# How to run Primer3

1. Ensure you have a correctly formatted input file (see [primer3input_example.txt](primer3input_example.txt) for an example)
2. Ensure you are logged in to the life sciences server (see the useful notes page) 
3. Run primer 3 with the following command
```primer3_core < inputfile > resultsfile```

The output file is in BoulderIO format. This is a series of 
```PARAMETER=Value```
lines

Easy parsing for a *single* target:
```results={}
fh=open(resultsfile)
for line in fh.readlines():
	(key,value)=line.strip().split('=',1)
	if key:
		results[key]=value

primercount=int(results['PRIMER_COUNT']) #check this
for p in range(primercount):
	left=results['PRIMER_LEFT_SEQUENCE_%s'%p] #check this. Also look at string substituion in 'string methods' on docs.python.org to see what %s does
```
 and so on to extract the features into e.g. a table

to append to a file use ```outfh=open('outfile','a')```


