import json

def convert_json(data):
	total_dict = []	
	keys = [d for d in data[0]]
	all_keys= keys[:-2] + ['type','date']
	index_dict = {}
	for index, key in zip(range(13), all_keys):
		index_dict[str(index)]=key
	for count, line in enumerate(data):
		dict_now = {}
		for coun ,lin in enumerate(line):
			coun = str(coun)
			dict_now[index_dict[coun]] = lin
		total_dict.append(dict_now)

	with open('customers.json', 'w') as json_file:
			json.dump(total_dict, json_file)