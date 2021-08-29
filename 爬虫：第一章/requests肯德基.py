import requests
import json
if __name__ == '__main__':
    url = 'https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}
    data = {
        'cname':'',
        'pid':'',
        'keyword': '北京',
        'pageIndex': '1',
        'pageSize': '10',
    }
    response = requests.post(url=url,params=data,headers=headers)

    list_data = response.json()

    fp = open('肯德基.json', 'w', encoding='utf-8')

    json.dump(list_data, fp=fp, ensure_ascii=False)

    print('1')
