output_a=open("species_a_rs.restrict", "w")
output_b=open("species_b_rs.restrict", "w")

#setting a variable to the position of the restriction site in species_a/species_b
pos_a=0
pos_b=0

#loop
while sites_a[pos_a]['gapstart'] < len(sites_a):
    if sites_a[pos_a]['gapstart'] == sites_b[pos_b]['gapstart']:
        pos_a += 1
        pos_b += 1
    elif sites_a[pos_a]['gapstart'] < sites_b[pos_b]['gapstart']:
        output_a.write("\n".join(sites_a[pos_a]))
        pos_a += 1
    elif sites_a[pos_a]['gapstart'] > sites_b[pos_b]['gapstart']:
        output_b.write("\n".join(sites_b[pos_b]))
        pos_b += 1

output_a.close()
output_b.close()