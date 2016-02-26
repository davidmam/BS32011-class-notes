import emboss_read
import align_emboss

jalview_ff=open('features_f.txt','w')
jalview_ff.write('restrictionsite\t00FFF3\n')

renzyme_list = ['SgeI', 'FaiI', 'MspJI', 'SetI', 'Tsp45I', 
                'EcorII', 'TfiI', 'HindII', 'SfeI', 'SphI', 
                'LpnPI', 'BmgT120I', 'DrdI', 'NspI']

for range(4438,13338) in output_a:
    if sites_a.startswith(renzyme_list) in output_a:
        sites_a.append.replace('')
    else:
        output_a.write(sites_a.append + "\n")
        jalview_ff.write(jalview_out(sites_a[pos_b], species_b)+'\n')