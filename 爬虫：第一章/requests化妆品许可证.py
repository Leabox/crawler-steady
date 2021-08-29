import requests
import json
if __name__ == '__main__':
     url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
     headers = {
         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
     }
     id_list = []

for page in range(1,6):
    page = str(page)
data = {
         'on': 'true',
         'page': page,
         'pageSize': '15',
         'productName':'',
         'conditionType': '1',
         'applyname':'',
         'applysn':'',
     }
json_ids = requests.post(url=url, headers=headers, data=data).json()
json_ids = requests.post(url=url,headers=headers,data=data).json()

for dic in json_ids['list']:
    id_list.append(dic['ID'])

    post_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
for id in id_list:
    data = {
         'id':id
     }

    detail_json = requests.post(url=post_url,headers=headers,data=data).json()
    print(detail_json,'------------------------------------------1------------------------------------------------------')
    all_data_list = []
    all_data_list.append(detail_json)
    fp = open('allData.json', 'w', encoding='utf-8')
    json.dump(all_data_list,fp=fp,ensure_ascii=False)
    print('okokokokokokokokokokok')