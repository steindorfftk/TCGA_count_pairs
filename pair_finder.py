import os

patients = {}

project = 'CHOL'
gene = 'CDKN2A'

with open(project+'.tsv','r') as texto:
	for line in texto:
		linha = line.split()
		if linha[8] not in patients.keys():
			patients[linha[8]]={}
		if linha[-1] == 'Normal':
			patients[linha[8]]['Normal'] = linha[0]
		else:
			patients[linha[8]]['Tumoral'] = linha[0]

paired_patients = {}

for key, value in patients.items():
	if 'Normal' in value.keys() and 'Tumoral' in value.keys():
		paired_patients[key] = {'Normal':value['Normal'],'Tumoral':value['Tumoral']}
		
for key, value in paired_patients.items():
	files = os.listdir(project+'/'+value['Normal'])
	with open(project+'/'+value['Normal']+'/'+files[0]) as texto:
		for line in texto:
			linha = line.split()
			if gene == linha[1]:
				paired_patients[key]['Normal Count'] = linha[6]
	files = os.listdir(project+'/'+value['Tumoral'])
	with open(project+'/'+value['Tumoral']+'/'+files[0]) as texto:
		for line in texto:
			linha = line.split()
			if gene == linha[1]:
				paired_patients[key]['Tumoral Count'] = linha[6]
				
with open('Paired_counts.csv','w') as texto:
	texto.write('ID;Normal;Tumoral\n')
	for key, value in paired_patients.items():
		texto.write(key + ';' + value['Normal Count'] + ';' + value['Tumoral Count'] + '\n')
	
	
	
	
	
	
	
	
	
	
	
