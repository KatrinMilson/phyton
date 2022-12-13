from bs4 import BeautifulSoup
import urllib.request

req = urllib.request.urlopen('https://www.ntv.ru/')
html = req.read()

soup = BeautifulSoup(html, 'html.parser')

news_s = soup.find_all('li', class_='visible')  # видео
news = soup.find_all('li', class_='permute')  # за_минуту
news_g = soup.find_all('div', class_ ="content")
news_e = soup.find_all('div', class_ ="caparison")

results = []

for A in news_s:
    title1 = A.find('a').get_text(strip=True)  # все статьи сверху
    desc1 = A.find('time').get_text(strip=True)  # time
    href1 = A.a.get('href')  # ссылки
    results.append({
        'title': title1,
        'desc': desc1,
        'href': href1,
    })

for item in news:
    title = item.find('p', class_='inure_p').get_text(strip=True)  # все с татьи с ЗаМинуту
    desc = item.find('a', class_='inure').get_text(strip=True)  # текст статьи
    href = item.a.get('href')  # ссылки
    results.append({
        'title': title,
        'desc': desc,
        'href': href,
    })

for B in news_g:
    title2 = B.find('li').get_text(strip=True)  # все статьи Главныетемы
    href2 = B.a.get('href')  # ссылки
    results.append({
        'title': title2,
        'href': href,
    })

for C in news_e:
    title3 = B.find('div', class_ = 'citem').get_text(strip=True)  # все статьи в эфире
    href3 = B.a.get('href')  # ссылки
    results.append({
        'title': title2,
        'href': href,
    })

f = open('news', 'w', encoding='utf-8')
i = 1
for A in results:
    f.write(f'\n\nНазвание:{A["title"]}\nОписание: {A["desc"]}\nСсылка: {A["href"]}\n\n********************\n')
    i += 1
    for item in results:
        f.write(f'\n\nНазвание:{item["title"]}\nОписание: {item["desc"]}\nСсылка: {item["href"]}\n\n********************\n')
        i += 1
        for B in results:
            f.write(f'\n\nНазвание:{B["title"]}}\nСсылка: {B["href"]}\n\n********************\n')
            i += 1
            for C in results:
                f.write(f'\n\nНазвание:{C["title"]}}\nСсылка: {C["href"]}\n\n********************\n')
                i += 1
f.close()