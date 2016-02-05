# list of dictionaries for species_a
species_a=[{'Start': 1, 'End': 6 , 'Name': 'MjaIV', 'Pattern':'GTNNAC', 'gapstart': 3},
           {'Start': 1, 'End': 6 , 'Name': 'HpaI', 'Pattern':'GTTAAC', 'gapstart': 4},
           {'Start': 1, 'End': 6 , 'Name': 'HindII', 'Pattern':'GTYRAC', 'gapstart': 6},
           {'Start': 2, 'End': 5 , 'Name': 'MseI', 'Pattern':'TTAA', 'gapstart': 6},
           {'Start': 5, 'End': 8 , 'Name': 'TaiI', 'Pattern':'ACGT', 'gapstart': 7}]
        
# list of dictionaries for species_b
species_b=[{'Start': 2, 'End': 5 , 'Name': 'MseI', 'Pattern':'TTAA', 'gapstart': 3},
           {'Start': 9, 'End': 12 , 'Name': 'SetI', 'Pattern':'ASST', 'gapstart': 3},
           {'Start': 9, 'End': 12 , 'Name': 'CviJI', 'Pattern':'RGCY', 'gapstart': 4},
           {'Start': 9, 'End': 12 , 'Name': 'AluBI', 'Pattern':'AGCT', 'gapstart': 5},
           {'Start': 11, 'End': 14 , 'Name': 'MspJI', 'Pattern':'CNNR', 'gapstart': 7}]

output_a=open("species_a_rs.restrict", "w")
output_b=open("species_b_rs.restrict", "w")

#setting a variable to the position of the restriction site in species_a/species_b
pos_a=0
pos_b=0

#loop
while species_a[pos_a]['gapstart'] < len(species_a):
    if species_a[pos_a]['gapstart'] == species_b[pos_b]['gapstart']:
        pos_a += 1
        pos_b += 1
    elif species_a[pos_a]['gapstart'] < species_b[pos_b]['gapstart']:
        output_a.write("\n".join(species_a[pos_a]))
        pos_a += 1
    elif species_a[pos_a]['gapstart'] > species_b[pos_b]['gapstart']:
        output_b.write("\n".join(species_b[pos_b]))
        pos_b += 1

output_a.close()
output_b.close()