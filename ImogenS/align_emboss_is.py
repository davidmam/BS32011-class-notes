#imports the other script instead of merging two scripts
import emboss_read_is
seq_dir = '../ImogenS/' #directory of information

#stating the filename of each species
species_a =  "m_erminea"
species_b =  "m_nivalis"

#retrieve and access 'sites' using 'getsites' function and stating what files to use
#x for a max value in restrict
esites_a = emboss_read_is.getsites(seq_dir + species_a + '_16.restrict', seq_dir + species_a + '.fasta')
esites_b = emboss_read_is.getsites(seq_dir + species_b + '_16.restrict', seq_dir + species_b + '.fasta')


#opens files ready to write to 
output_a=open(species_a+".output", "w")
output_b=open(species_b+".output", "w")

#function to write out to a new file for Jalview purposes
jalview_uf=open('features_uf.txt','w')

#colour in unique restriction sites with magenta on Jalview
jalview_uf.write('restrictionsite\tff00ff\n')

#setting the position in the list of dictionaries
pos_a = 0
pos_b = 0

#setting a counter to know how many unique restriction sites saved
counter_a = 0
counter_b = 0

#defining a function that displays selected information from 'sites'

def formatsite(site):
    if site['gappedstart'] >= 4438 and site['gappedstart'] <= 13338: #only looks at sites in the conserved region
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


#two new files containing unique restriction sites and a 'features.txt' file (imported into Jalview) to highlight them in Jalview
species_a_unique=[]
species_b_unique=[]


enzymename = ['AgeI', 'PasI', 'KflI', 'PspXI', 'NaeI', 'BsrDI', 'AlwNI', 'Eco47III', 
'KpnI', 'PruI', 'MroNI', 'Acc65I', 'MluI', 'BamHI', 'SalI', 'AlfI', 'EcoRI', 'BasAI', 
'BglII', 'PsrI', 'PfoI', 'BcgI'] #list of suitable enzymes selected from running the code with an empty list (that returned all sites) previously

allcutters=set(list(esites_a.keys())+list(esites_b.keys()))
allsites_a=[]
allsites_b=[]
for enzymelist in allcutters:
    if enzymename and enzymelist not in enzymename: #selects enzymes only in enzymelist to write to file
        continue
    pos_a=0
    pos_b=0
    if enzymelist not in esites_a:
        #write in unique to b file
        for s in esites_b[enzymelist]:
            output_b.write(formatsite(s)+ "\n")
            jalview_uf.write(jalview_out(s, species_b)+'\n')
        counter_b += len(esites_b[enzymelist])-1 #keeping track of number of sites unique to b
        species_b_unique+=esites_b[enzymelist][:-1]
        allsites_b+=esites_b[enzymelist][:-1]
    elif enzymelist not in esites_b:
        print('unique in A')
        for s in esites_a[enzymelist]:
            output_a.write(formatsite(s)+ "\n") #unique to species a printed to file
            jalview_uf.write(jalview_out(s, species_a)+'\n')
        counter_a += len(esites_a[enzymelist])-1 #keeping track of number of sites unique to a 
        species_a_unique+=esites_a[enzymelist][:-1]
        allsites_a+=esites_a[enzymelist][:-1]

    else:
        sites_a = esites_a[enzymelist]
        sites_b = esites_b[enzymelist]
        allsites_a=allsites_a+sites_a[:-1]#strip off fake end added in emboss_read
        allsites_b+=sites_b[:-1]#strip off fake end added in emboss_read
        print('comparing enzymes')
        while pos_a < len(sites_a):
            if sites_a[pos_a]['gappedstart'] == sites_b[pos_b]['gappedstart']:
                pos_a += 1
                pos_b += 1
            elif sites_a[pos_a]['gappedstart'] < sites_b[pos_b]['gappedstart']:
                output_a.write(formatsite(sites_a[pos_a])+ "\n")
                pos_a += 1
                counter_a += 1
                species_a_unique.append(sites_a[pos_a]) #write to unique in a 
                print('unique A')
                jalview_uf.write(jalview_out(sites_a[pos_a], species_a)+'\n')
            elif sites_a[pos_a]['gappedstart'] > sites_b[pos_b]['gappedstart']:
                output_b.write(formatsite(sites_b[pos_b])+ "\n")
                pos_b += 1
                counter_b += 1
                species_b_unique.append(sites_b[pos_b]) #write to unique in b
                jalview_uf.write(jalview_out(sites_b[pos_b], species_b)+'\n')
print(species_a + str(counter_a))
print(species_b + str(counter_b))

output_a.close()
output_b.close()

jalview_uf.close()
#output files created
output_af=open("m_erminea.restrict", "w") 
output_bf=open("m_nivalis.restrict", "w")

toomanycuts = 5
enzymecount={'END':{'all_a':1,'all_b':1,'unique_a':1,'unique_b':1}}

#creates table in IPython console that shows number of sites in a, unique to a, number of sites in b, unique to b
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

for v in enzymecount.keys():
    if int(enzymecount[v]['all_a']) <= toomanycuts and int(enzymecount[v]['all_b']) <= toomanycuts :
        print('%s\t%s\t%s\t%s\t%s\n'%(v,enzymecount[v]['all_a'],enzymecount[v]['unique_a'],enzymecount[v]['all_b'],enzymecount[v]['unique_b']))
