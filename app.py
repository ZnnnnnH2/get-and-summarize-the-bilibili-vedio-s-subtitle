import convert_headers
import cook_raw_subtitile
import get_raw_subtitle
import get_aid_and_cid
import os
from openai import OpenAI

choice1 = int(input("need convert headers? 1 for yes, 0 for no: "))
if choice1 == 1:
	print("please put your raw headers in raw_headers.txt")
	convert_headers.convert_headers()
else:
	print("please put your headers in headers.json")

choice2 = int(input("convert by bV or aid/cid? 1 for bv, 0 for the other: "))
aid, cid = 0, 0

if choice2 == 1:
	print("please put your BV in the following input")
	bv = input()
	convert_headers.convert_headers()
	aid, cid = get_aid_and_cid.get_aid_and_cid_by_bv(bv)
else:
	aid = input("please put your aid: ")
	cid = input("please put your cid: ")

get_raw_subtitle.get_raw_subtitle(aid, cid)
cook_raw_subtitile.cook_raw_subtitle()
print('字幕已保存到 subtitile.txt')
choice3 = int(input("need ai to summerize it? 1 for yes, 0 for no: "))


def get_key():
	with open('OPENAI_API_KEY', 'w+', encoding='utf-8') as f:
		api_key = f.read().strip()
		if not api_key:
			api_key = input("输入您的 OpenAI API 密钥")
			f.write('OPENAI_API_KEY')
	return api_key


if choice3 == 1:
	api_key = get_key()
	client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")
	contents = open('subtitile.txt', 'r', encoding='utf-8').read()
	response = client.chat.completions.create(
		model="deepseek-reasoner",
		messages=[
			{"role": "system", "content": "You are a assistant, help me to summarize the subtitle as detailed as possible, in the end give me some suggestions"},
			{"role": "user", "content": contents},
		],
		stream=False
	)
	with open('summary.txt', 'w', encoding='utf-8') as f:
		f.write(response.choices[0].message.content)
