import csv
def convert_csv(data):	
	header = data[0][:-2] + ['type','date']
	with open('customers.csv', 'w') as file:
		writer = csv.writer(file)
		writer.writerow(header)
		for count, pro in enumerate(data):
			if count == 0:
				print(pro)
				continue
			writer.writerow(pro)