import requests as req
import time

keyword=input('請輸入關鍵字:')
t = time.time()
url='https://www.ptt.cc/bbs/NTUcourse/search?q='+keyword
print(url)
while True:
    try:
        html=req.get(url)
        import bs4
        root=bs4.BeautifulSoup(html.text,'html.parser')
        titles=root.find_all('div',class_='title')
        for title in titles:
            if title.a.string != None:
                print(title.a.string)
                titlelinks=root.find('a', string=title.a.string)
                print('https://www.ptt.cc'+titlelinks['href'])
        nextlink=root.find('a',string='‹ 上頁')
        url='https://www.ptt.cc'+ nextlink['href']
    except:
        break

print('\n搜尋完畢！共花費',time.time()-t,'秒')