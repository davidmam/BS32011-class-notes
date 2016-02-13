#imports the other script instead of merging two scripts
import emboss_read
seq_dir = '../sequences/individual/'

#stating the filename of the species
species_a =  "e_europaeus"
species_b =  "s_vulgaris"

#retrieve and access 'sites' using 'getsites' function and stating what files to use
sites_a = emboss_read.getsites(seq_dir + species_a + '.restrict', seq_dir + species_a + '.fasta')
sites_b = emboss_read.getsites(seq_dir + species_b + '.restrict', seq_dir + species_b + '.fasta')

#stating functions to write out unique restriction sites
output_a=open("e_europaeus_rs.restrict", "w")
output_b=open("s_vulgaris_rs.restrict", "w")
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

while pos_a < len(sites_a):
    if sites_a[pos_a]['gappedstart'] == sites_b[pos_b]['gappedstart']:
        pos_a += 1
        pos_b += 1
    elif sites_a[pos_a]['gappedstart'] < sites_b[pos_b]['gappedstart']:
        output_a.write(formatsite(sites_a[pos_a])+ "\n")
        pos_a += 1
        counter_a += 1
        species_a_unique.append(sites_a[pos_a])
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
enzymecount={}
for s in sites_a:
    try:
        enzymecount[s['Enzyme_name']]['all_a']+=1
        enzymecount[s['Enzyme_name']]['all_b']+=1
        enzymecount[s['Enzyme_name']]['unique_a']+=1
        enzymecount[s['Enzyme_name']]['unique_b']+=1
    except:
        enzymecount[s['Enzyme_name']]={'all_a':1,'all_b':0,'unique_a':0,'unique_b':0}
        enzymecount[s['Enzyme_name']]={'all_a':0,'all_b':1,'unique_a':0,'unique_b':0}
        enzymecount[s['Enzyme_name']]={'all_a':0,'all_b':0,'unique_a':1,'unique_b':0}
        enzymecount[s['Enzyme_name']]={'all_a':0,'all_b':0,'unique_a':0,'unique_b':1}

# after getting the count
output_af=open("e_europaeus_rsf.restrict", "w")
output_bf=open("s_vulgaris_rsf.restrict", "w")

toomanycuts = 10
for site in enzymecount:
    if enzymecount[s['Enzyme_name']['unique_a']] <= toomanycuts:
        output_af.write(formatsite(sites_a['Enzyme_name'])+ "\n")
        jalview_uf.write(jalview_out(sites_a[pos_a], species_a)+'\n')

#function to write out to a new file for Jalview purposes
jalview_f=open('features_f.txt','w')

#colour in unique restriction sites with magenta on Jalview
jalview_f.write('restrictionsite\t00FFF3\n')