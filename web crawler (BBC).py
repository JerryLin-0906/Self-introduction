import urllib.request as req
url='https://www.bbc.com/news'
request=req.Request(url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'})
with req.urlopen(request) as response:
    data=response.read().decode()
#print(data)
import bs4
root=bs4.BeautifulSoup(data,'html.parser')
titles=root.find('h3',class_='gs-c-promo-heading__title gel-paragon-bold nw-o-link-split__text')
print(titles.string)
titlelinks=root.find('a', string=titles.string)
print('https://bbc.com'+titlelinks['href'])

subtitles=root.find_all('h3',class_='gs-c-promo-heading__title gel-pica-bold nw-o-link-split__text')

for subtitle in subtitles:
    ss=subtitle.string
    links=root.find_all('a', string=ss)
    n=len(links)

    if n ==0:
        print(ss)
        
    elif n >= 1:
        print(ss)
        print('https://bbc.com'+links[0]['href'])
