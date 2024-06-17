import json
import pprint

subtitle_dict = json.load(open('xxx.json', encoding='utf-8'))
subtitle_body = subtitle_dict['body']

subtitle_need = {}

for i in subtitle_body:
    subtitle_need[i['content']] = str(i['from']) + '秒' + '--' + str(i['to']) + '秒'

pprint.pprint(subtitle_need)
