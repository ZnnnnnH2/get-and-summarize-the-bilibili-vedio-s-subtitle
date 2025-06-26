import requests

def get_aid_and_cid_by_bv(bv):
	if bv[0:2] == 'BV':
		bv = bv[2:]
	# url = f'https://api.bilibili.com/x/web-interface/view?bvid=BV{bv}'
	url = f'https://api.freejk.com/shuju/bv-a-c/?bvid={bv}'
	response = requests.get(url).json()
	aid = response['aid']
	cid = response['cid']
	return aid, cid

if __name__ == '__main__':
	# bv = input('请输入BV号: ')
	bv = 'BV1TTMUzHEFu'
	aid, cid = get_aid_and_cid_by_bv(bv)
	print(f'视频的AV号是: {aid}, CID是: {cid}')