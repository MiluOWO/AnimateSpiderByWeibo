import requests
import re
import json
r = requests.get('https://m.weibo.cn/api/container/getIndex?type=uid&value=5580632206&containerid=1076035580632206')
data = json.loads(r.text)
Animate=['刀剑神域','青春猪头少年','魔法禁书']
ReRegular=re.compile(r'magnet:\?xt=urn\:btih\:.{39}[0-9A-Z]')
AriaUrl = 'http://127.0.0.1:6800/jsonrpc'
headers = {'Host': '127.0.0.1:6800',
		   'Origin': 'http://127.0.0.1',
		   'Content-Type': 'application/json;charset=UTF-8'}
def read1():
	filename = '/home/pi/Desktop/link1.txt'
	with open(filename,'r') as file:
		content = file.read()
		#print(content)	
	return content

content = read1()
filename = '/home/pi/Desktop/link1.txt'
with open(filename,'a') as file:
	for i in data['data']['cards']:
		temp = i['mblog']['text']
		for j in Animate:
			if(j in temp):		
				link = ReRegular.search(i['mblog']['text'])
				forwrite=link.group()+'\n'
				if(link.group() not in content):
					file.write(forwrite)
					#print(j,link.group())
					json_data = json.dumps([{"jsonrpc":"2.0","method":"aria2.addUri","id":"QXJpYU5nXzE1NDIyNTkwNzhfMC45NjU1OTYyMTkyMzEyNzQx","params":["token:root233",[link.group()],{}]}]) 
					#print(json_data)
					u = requests.post(AriaUrl,data=json_data,headers=headers)
					#print(u.status_code)
print('run OK')

