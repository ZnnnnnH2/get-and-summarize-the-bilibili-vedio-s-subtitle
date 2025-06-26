import json

def convert_headers():
	with open('raw_headers.txt', 'r', encoding='utf-8') as f:
		dic = {}
		for line in f:
			if line.strip():
				try:
					key, value = line.split(': ', 1)
					dic[key] = value.strip()
				except:
					print(f'Error processing line: {line.strip()}')
					continue
		with open('header.json', 'w', encoding='utf-8') as ff:
			json.dump(dic, ff, ensure_ascii=False, indent=4)
