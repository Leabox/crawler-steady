import requests
import json
if __name__ == '__main__':
    post_url = 'https://fanyi.baidu.com/sug'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36' }
    word = input('enter a word:')
    data={
       'kw':word
    }
    response = requests.post(url=post_url,data=data,headers=headers)
    #json返回的是一个对象obj

    dic_obj = response.json()
    print(dic_obj)
    fp = open('dog.json', 'w', encoding='utf-8')
    json.dump(dic_obj,fp=fp,ensure_ascii=False)
    print('1')
