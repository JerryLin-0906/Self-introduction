import requests as req
import time
from multiprocessing import Process
import numpy as np
import bs4

def ptt(page,keyword):
    url = 'https://www.ptt.cc/bbs/NTUcourse/search?page=' + str(page) + '&q=' + keyword
    html = req.get(url)
    root = bs4.BeautifulSoup(html.text, 'html.parser')
    titles = root.find_all('div', class_='title')
    for title in titles:
        if title.a.string != None:
            print(title.a.string)
            titlelinks = root.find('a', string=title.a.string)
            print('https://www.ptt.cc' + titlelinks['href'])
def pagenum(keyword):
    url = 'https://www.ptt.cc/bbs/NTUcourse/search?q=' + keyword
    html = req.get(url)
    root = bs4.BeautifulSoup(html.text, 'html.parser')
    roldlink = root.find('a', string='最舊')
    oldlink = roldlink['href'].replace('&', '=').split('=')
    pagenum = oldlink[1]
    return int(pagenum)+1

pro = []
if __name__ == '__main__':
    keyword = input('請輸入關鍵字:')
    t = time.time()
    pagenum = pagenum(keyword)

    for page in range(1,pagenum):

        p = Process(target=ptt, args=(page,keyword,))
        pro.append(p)
        p.start()

    for process in pro:
        process.join()

    print('\n搜尋完畢！共花費',time.time()-t,'秒')
