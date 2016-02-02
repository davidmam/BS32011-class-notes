#script that finds restriction sites, which appear in only one of two sequences when given the data; Maxim, Imogen
#script to write the file

#challenges:
##sequences are gapped

alignedseqpos==(start+gaps)

#loop 
while alignedseqpos:
	#add to aligned sequence position
	#remember the start site, how many gaps are included
read in all data:
	#add to each entry
	#aligned.start -> start pos in gapped sequence 

seqpos1=1
pos2=0
seqpos2=1
for pos1 in range(len[list1]):
	#does entry at list1(pos1) match entry at list2(pos2)
	#if true add 1 to pos2 and try loop again -> pos1 will increment
	#list1[pos1][start]>list2[pos2][start] -> extra site in list2 then add to a list of seq2 specific sites

species_a = ['GTNNAC', 'GTTACC', 'GTYRAC', 'TTAA', 'ACGT']
species_b = ['TTAA', 'ASST', 'RGCY', 'AGCT', 'CNNR']

output_a=open("species_a_rs.restrict", "w")
output_b=open("species_b_rs.restrict", "w")

pos=0 #setting a variable to the position of the restriction site

for species_a[pos] in range(len[species_a]):
    if species_a[pos]==species_b[pos]:
        pos += 1
    elif species_a[pos] < species_b[pos]:
        outputa.write("\n".join(species_a[pos])) #adding unique restriction site based on current position
    elif species_a[pos] > species_b[pos]:
        while species_a[pos] > species_b[pos]:
            output_b.write("\n".join(species_b[pos]))
            pos += 1

output_a.close()
output_b.close()

and species_b[pos] in range (len[species_b])

a=[10, 11, 12, 13, 14, 15]
outputa.write[a[i] for i in (1,2,5)]
