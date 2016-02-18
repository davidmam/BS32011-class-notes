#imports the other script instead of merging two scripts
import emboss_read
seq_dir = '../sequences/individual/'

#stating the filename of the species
species_a =  "l_europaeus"
species_b =  "f_silvestris"

#retrieve and access 'sites' using 'getsites' function and stating what files to use
esites_a = emboss_read.getsites(seq_dir + species_a + '_16.restrict', seq_dir + species_a + '.fasta')
esites_b = emboss_read.getsites(seq_dir + species_b + '_16.restrict', seq_dir + species_b + '.fasta')

#ideas 
# change sites_x from [ {site1}, {site2}] to
# {'enzyme1': [{site1}, {site2}],'Enzyme2':[{site1},{site2}]}


#stating functions to write out unique restriction sites
output_a=open(species_a+".output", "w")
output_b=open(species_b+".output", "w")
#function to write out to a new file for Jalview purposes
jalview_uf=open('features_uf.txt','w')

#colour in unique restriction sites with magenta on Jalview
jalview_uf.write('restrictionsite\tff00ff\n')

#setting the position in the list of dictionaries
pos_a=0
pos_b=0

#setting a counter to know how many unique restriction sites saved
counter_a = 0
counter_b = 0

#defining a function that displays selected information from 'sites'

def formatsite(site):
    if site['gappedstart'] >= 4438 and site['gappedstart'] <= 13338:
        return '|'.join([str(site['Start']), str(site['gappedstart']), 
              site['Enzyme_name'], site['Restriction_site']])
    else:
        return ''

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
allcutters=set(list(esites_a.keys())+list(esites_b.keys()))
allsites_a=[]
allsites_b=[]
for enzyme in allcutters: # change this to a list of interesting enzymes if you wish
    pos_a=0
    pos_b=0
    if enzyme not in esites_a:
        #write out as unique b
        for s in esites_b[enzyme]:
            output_b.write(formatsite(s)+ "\n")
            jalview_uf.write(jalview_out(s, species_b)+'\n')
        counter_b += len(esites_b[enzyme])-1
        species_b_unique+=esites_b[enzyme][:-1]
        allsites_b+=esites_b[enzyme][:-1]
    elif enzyme not in esites_b:
        print('unique in A')
        for s in esites_a[enzyme]:
            output_a.write(formatsite(s)+ "\n")
            jalview_uf.write(jalview_out(s, species_a)+'\n')
        counter_a += len(esites_a[enzyme])-1
        species_a_unique+=esites_a[enzyme][:-1]
        allsites_a+=esites_a[enzyme][:-1]
#write out as unique_a
    else:
        sites_a = esites_a[enzyme]
        sites_b = esites_b[enzyme]
        allsites_a=allsites_a+sites_a[:-1]#strip off fake end
        allsites_b+=sites_b[:-1]#strip off fake end
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

output_af=open("l_europaeus.restrict", "w")
output_bf=open("f_silvestris.restrict", "w")

toomanycuts = 5
enzymecount={'END':{'all_a':1,'all_b':1,'unique_a':1,'unique_b':1}}
regionstart=4500
regionend=1400
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

toomanycuts=5

for v in enzymecount.keys():
    if int(enzymecount[v]['all_a']) <= toomanycuts and int(enzymecount[v]['all_b']) != int(enzymecount[v]['all_a']) :
        print('%s\t%s\t%s\t%s\t%s\n'%(v,enzymecount[v]['all_a'],enzymecount[v]['unique_a'],enzymecount[v]['all_b'],enzymecount[v]['unique_b']))
    
