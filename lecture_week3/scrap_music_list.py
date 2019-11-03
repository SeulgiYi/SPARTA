import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta


url = 'https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20190908'
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(url, headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')
music_chart = soup.select('#body-content > div.newest-list > div.music-list-wrap > table > tbody > tr')

for music in music_chart:
    music_rank = music.select_one('td.number').text.split()
    music_info = music.select_one('td.info')
    info_tag = music_info.select('a')
    title = info_tag[0].text.strip()
    artist = info_tag[1].text.strip()
    album_title = info_tag[2].text.strip()
    print(music_rank, title, artist, album_title)
    doc = {
        'rank': music_rank[0],
        'rank_variation': music_rank[1],
        'title': title,
        'artist': artist,
        'album_title': album_title
    }
    db.genie_music.insert_one(doc)



db_check = db.genie_music
print(db_check)









