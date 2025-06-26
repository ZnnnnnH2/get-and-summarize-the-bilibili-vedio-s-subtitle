import requests
import json


def get_raw_subtitle(aid, cid):
	hdrs = json.load(open('header.json', 'r', encoding='utf-8'))
	url = f'https://api.bilibili.com/x/player/wbi/v2?aid={aid}&cid={cid}'
	j = requests.get(url, headers=hdrs).json()
	subtitles = j['data']['subtitle']['subtitles']
	prefs = [s for s in subtitles if s['lan'] in ['ai-zh', 'zh']]
	if not prefs:
		print('无可用字幕')
		return
	url = 'https:' + prefs[0]['subtitle_url']
	sub = requests.get(url, headers=hdrs).json()
	with open('raw_subtitle.json', 'w', encoding='utf-8') as ff:
		json.dump(sub, ff, ensure_ascii=False)


if __name__ == '__main__':
	# aid = input("please input your aid")
	# cid = input("please input your cid")
	aid = "114682673235142"
	cid = "30499472498"
	get_raw_subtitle(aid, cid)
