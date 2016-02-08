import emboss_read
seq_dir = '../sequences/individual/'
species_a =  "e_europaeus"
species_b =  "f_silvestris"
sites_a = emboss_read.getsites(seq_dir +species_a + '.restrict', seq_dir +species_a + '.fasta')
sites_b = emboss_read.getsites(seq_dir +species_b + '.restrict', seq_dir +species_b + '.fasta')
output_a=open("species_a_rs.restrict", "w")
output_b=open("species_b_rs.restrict", "w")
jalview=open('features.txt','w')

jalview.write('restrictionsite\tff00ff\n')


#setting a variable to the position of the restriction site in species_a/species_b
pos_a=0
pos_b=0

counter_a = 0
counter_b = 0

def formatsite(site):
    return '|'.join([str(site['Start']), str(site['gappedstart']), 
              site['Enzyme_name'], site['Restriction_site']])
def jalview_out(site, species):
    return '\t'.join([site['Enzyme_name'],species,'-1',
               str(site['gappedstart']),
            str(site['gappedstart']+len(site['Restriction_site'])),
                'restrictionsite'])
#loop
while sites_a[pos_a]['gappedstart'] < len(sites_a):
    if sites_a[pos_a]['gappedstart'] == sites_b[pos_b]['gappedstart']:
        pos_a += 1
        pos_b += 1
    elif sites_a[pos_a]['gappedstart'] < sites_b[pos_b]['gappedstart']:
        output_a.write(formatsite(sites_a[pos_a])+ "\n")
        pos_a += 1
        counter_a += 1
        jalview.write(jalview_out(sites_a[pos_a], species_a)+'\n')
    elif sites_a[pos_a]['gappedstart'] > sites_b[pos_b]['gappedstart']:
        output_b.write(formatsite(sites_b[pos_b])+ "\n")
        pos_b += 1
        counter_b += 1
        jalview.write(jalview_out(sites_b[pos_b], species_b)+'\n')

print(species_a + str(counter_a))
print(species_b + str(counter_b))

output_a.close()
output_b.close()
jalview.close()