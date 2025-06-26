import json


def cook_raw_subtitle():
	"""
Process the raw subtitle JSON file and save the contents to a text file.
	:return: NONE
	"""
	j = json.load(open('raw_subtitle.json', 'r', encoding='utf-8'))
	# print(j)
	body = j.get('body', {})
	with open('subtitile.txt', 'w', encoding='utf-8') as f:
		contents = [content['content'] for content in body]
		f.write('\n'.join(contents))


if __name__ == '__main__':
	cook_raw_subtitle()
