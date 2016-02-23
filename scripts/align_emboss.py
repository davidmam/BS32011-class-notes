#moderated by Simon Bajew on 23/02/2016#

import emboss_read
seq_dir = '../sequences/individual/'

#setting the species names
species_a =  "l_europaeus"
species_b =  "o_cuniculus"

#retrieving and accessing 'sites' using 'getsites' function and stating what files to use
esites_a = emboss_read.getsites(seq_dir + species_a + '_16.restrict', seq_dir + species_a + '.fasta')
esites_b = emboss_read.getsites(seq_dir + species_b + '_16.restrict', seq_dir + species_b + '.fasta')

#opening files for writing out unique restriction sites
output_a=open(species_a+".output", "w")
output_b=open(species_b+".output", "w")

#opening a file for writing out Jalview features file
jalview_uf=open('unflitered_features.txt','w')
jalview_uf.write('restrictionsite\tff00ff\n')

#setting the position in the list of dictionaries
pos_a = 0
pos_b = 0

#setting a counter for saved unique restriction sites
counter_a = 0
counter_b = 0

#defining a function that displays selected information from 'sites'
def formatsite(site):
        return '|'.join([str(site['Start']), str(site['gappedstart']), 
              site['Enzyme_name'], site['Restriction_site']])

#defining a function for output to be in jalview format
def jalview_out(site, species):
    return '\t'.join([site['Enzyme_name'],species,'-1',
               str(site['gappedstart']),
            str(site['gappedstart']+len(site['Restriction_site'])),
                'restrictionsite'])

#loop selects and saves restriction sites unique to both species
#two new files containing unique restriction sites and a 'features.txt' file (imported into Jalview) to highlight them in Jalview
species_a_unique=[]
species_b_unique=[]
#run this for each list in sites (by enzyme)
# eg. for enzyme in esites: (check enzyme cuts both species, if it doesn't then take that entire list as unique for that species)

#adding a list of suitable enzymes from printed output for specific species
enzymename = ["HgiCI", "Crf9I", "CsiI", "SfiI", "PmaCI", "KflI", "NarI", "EciI", "DinI", "SmaI", "AlfI", "BcgI", "KasI"] 

allcutters=set(list(esites_a.keys())+list(esites_b.keys()))
allsites_a=[]
allsites_b=[]

for enzymelist in allcutters: # change this to a list of interesting enzymes if you wish
    if enzymename and enzymelist not in enzymename:
        continue
    pos_a=0
    pos_b=0
    if enzymelist not in esites_a:
        
        #writting out as unique b
        for s in esites_b[enzymelist]:
            output_b.write(formatsite(s)+ "\n")
            jalview_uf.write(jalview_out(s, species_b)+'\n')
        counter_b += len(esites_b[enzymelist])-1
        species_b_unique+=esites_b[enzymelist][:-1]
        allsites_b+=esites_b[enzymelist][:-1]
    elif enzymelist not in esites_b:
        print('unique in A')
        for s in esites_a[enzymelist]:
            output_a.write(formatsite(s)+ "\n")
            jalview_uf.write(jalview_out(s, species_a)+'\n')
        counter_a += len(esites_a[enzymelist])-1
        species_a_unique+=esites_a[enzymelist][:-1]
        allsites_a+=esites_a[enzymelist][:-1]

#writing out as unique_a
    else:
        sites_a = esites_a[enzymelist]
        sites_b = esites_b[enzymelist]
        allsites_a=allsites_a+sites_a[:-1]#stripping off the fake End
        allsites_b+=sites_b[:-1]#stripping off the fake End
        print('comparing enzymes')
        while pos_a < len(sites_a):
            if sites_a[pos_a]['gappedstart'] == sites_b[pos_b]['gappedstart']:
                pos_a += 1
                pos_b += 1
            elif sites_a[pos_a]['gappedstart'] < sites_b[pos_b]['gappedstart']:
                output_a.write(formatsite(sites_a[pos_a])+ "\n")
                pos_a += 1
                counter_a += 1
                species_a_unique.append(sites_a[pos_a])
                print('unique A')
                jalview_uf.write(jalview_out(sites_a[pos_a], species_a)+'\n')
            elif sites_a[pos_a]['gappedstart'] > sites_b[pos_b]['gappedstart']:
                output_b.write(formatsite(sites_b[pos_b])+ "\n")
                pos_b += 1
                counter_b += 1
                species_b_unique.append(sites_b[pos_b])
                jalview_uf.write(jalview_out(sites_b[pos_b], species_b)+'\n')
print(species_a + str(counter_a))
print(species_b + str(counter_b))

output_a.close()
output_b.close()

jalview_uf.close()

output_af=open("l_europaeus_16.restrict", "w")
output_bf=open("o_cuniculus_16.restrict", "w")

#setting a cut-off for sites that cut more than 5 times
toomanycuts = 5

#counting restriction sites
enzymecount={'END':{'all_a':1,'all_b':1,'unique_a':1,'unique_b':1}}
for s in allsites_a:
    try:
        enzymecount[s['Enzyme_name']]['all_a']+=1
    except:
        enzymecount[s['Enzyme_name']]={'all_a':1,'all_b':0,'unique_a':0,'unique_b':0}

for s in allsites_b:
    try:
        enzymecount[s['Enzyme_name']]['all_b']+=1
    except:
        enzymecount[s['Enzyme_name']]={'all_a':0,'all_b':1,'unique_a':0,'unique_b':0}

for s in species_b_unique:
    enzymecount[s['Enzyme_name']]['unique_b']+=1
for s in species_a_unique:
    enzymecount[s['Enzyme_name']]['unique_a']+=1

#printing the table of all and unique sites
for v in enzymecount.keys():
    if int(enzymecount[v]['all_a']) <= toomanycuts and int(enzymecount[v]['all_b']) <= toomanycuts :
        print('%s\t%s\t%s\t%s\t%s\n'%(v,enzymecount[v]['all_a'],enzymecount[v]['unique_a'],enzymecount[v]['all_b'],enzymecount[v]['unique_b']))
