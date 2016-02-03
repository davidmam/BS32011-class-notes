species_a = ['MjaIV', 'HpaI', 'HindII', 'MseI', 'TaiI']
species_b = ['MseI', 'SetI', 'CviJI', 'AluBI', 'MspJI']

dict_a={'name':species_a}
dict_b={'name':species_b}

output_a=open("species_a_rs.restrict", "w")
output_b=open("species_b_rs.restrict", "w")

pos_a=0 #setting a variable to the position of the restriction site in species_a
pos_b=0 #setting a variable to the position of the restriction site in specoes_b

for dict_a('name'[pos_a]) in range(len[dict_a]):
    if dict_a('name'[pos_a])==dict_b('name'[pos_b]):
        pos_b += 1
    elif dict_a('name'[pos_a]) < dict_b('name'[pos_b]):
        output_a.write("\n".join(dict_a('name'[pos_a])) #adding unique restriction site based on current position
    elif dict_a('name'[pos_a]) > dict_b('name'[pos_b]):
        while dict_a('name'[pos_a]) > dict_b('name'[pos_b]):
            output_b.write("\n".join(dict_b('name'[pos_b]))
            pos_b += 1

output_a.close()
output_b.close()