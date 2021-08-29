
#门户网站的服务器载体身份标识

import requests
if __name__ =="__main__":
    #UA伪装：将对应的User-Agent
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
    }

    url = 'https://www.sogou.com/web?'
    kw = input('enter a word:')
    param = {
        'query':kw
    }
    #
    response = requests.get(url=url,params=param,headers=headers)
    page_text = response.text
    fileName = kw+'.html'
    with open(fileName,'w',encoding='utf-8') as fp:
        fp.write(page_text)
        print(fileName,'1')