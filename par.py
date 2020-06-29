import requests
from bs4 import BeautifulSoup
import csv
#
CSV = 'game.csv'
HOST = 'https://stopgame.ru'
URL = "https://stopgame.ru/review/new/stopchoice"

HEADERS = {
 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
 'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36'
}

def get_html(url, params=' '):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_= 'game-summary')
    game = []


    for item in items:
        game.append(
            {
                'title': item.find('div', class_='caption caption-bold').get_text(strip=True),
                'link': HOST + item.find('div', class_= 'caption caption-bold').find('a').get('href'),
                'image': it em.find('div', class_='image lazy').get('style')
            }
        )
    return game

def save_doc(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Название обзора', 'Ссылка на обзор', 'Изображение обзора'])
        for item in items:
            writer.writerow([item['title'], item['link'],item['image']])

def parser():
    PAGENATION = input('Укажите количество страниц для парсинга: ')
    PAGENATION = int(PAGENATION.strip())
    html = get_html(URL)
    if html.status_code == 200:
        game = []
        for page in range(1, PAGENATION):
            print (f'Парсим страницу: {page}')
            html = get_html(URL, params={'page': page})
            game.extend(get_content(html.text))
            save_doc(game, CSV)
        print (game)
    else:
        print('Error')

parser()
