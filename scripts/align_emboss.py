#imports the other script instead of merging two scripts
import emboss_read
seq_dir = '../sequences/individual/'

#stating the filename of the species
species_a =  "l_europaeus"
species_b =  "f_silvestris"

#retrieve and access 'sites' using 'getsites' function and stating what files to use
sites_a = emboss_read.getsites(seq_dir + species_a + '.restrict', seq_dir + species_a + '.fasta')
sites_b = emboss_read.getsites(seq_dir + species_b + '.restrict', seq_dir + species_b + '.fasta')

#stating functions to write out unique restriction sites
output_a=open("l_europaeus.restrict", "w")
output_b=open("f_silvestris.restrict", "w")
#function to write out to a new file for Jalview purposes
jalview_uf=open('features_uf.txt','w')

#colour in unique restriction sites with magenta on Jalview
jalview_uf.write('restrictionsite\tff00ff\n')

#setting the position in the list of dictionaries
pos_a=4438
pos_b=4438

#setting a counter to know how many unique restriction sites saved
counter_a = 0
counter_b = 0

#defining a function that displays selected information from 'sites'

def formatsite(site):
    if site['gappedstart'] >= 4438 and site['gappedstart'] <= 13338:
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

output_af=open("l_europaeus.restrict", "w")
output_bf=open("f_silvestris.restrict", "w")

toomanycuts = 5
enzymecount={}

for s in sites_a:
    try:
        enzymecount[s['Enzyme_name']]['all_a']+=1
    except:
        enzymecount[s['Enzyme_name']]={'all_a':1,'all_b':0}

for s in sites_b:
    try:
        enzymecount[s['Enzyme_name']]['all_b']+=1
    except:
        enzymecount[s['Enzyme_name']]={'all_a':0,'all_b':1}


for v in enzymecount:
    if int(v['all_a']) <= toomanycuts:
        output_af.write(formatsite(sites_a['Enzyme_name'])+ "\n")
        jalview_uf.write(jalview_out(sites_a, species_a)+'\n')
    elif v['all_b'] <= toomanycuts:
        output_bf.write(formatsite(sites_b['Enzyme_name'])+ "\n")
        jalview_uf.write(jalview_out(sites_b, species_a)+'\n')
