import requests
from bs4 import BeautifulSoup

def billboard():
    url="https://www.billboard.com/charts/hot-100/"
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    songs=soup.select('.o-chart-results-list__item > #title-of-a-story')
    #print(soup)
    #print(songs)

    song_list = [s.getText().strip("\n \t") for s in songs]
    #print(song_list)

    return song_list




def melon():
    url="https://www.melon.com/chart/index.htm"
    header = {'user-agent':
                  'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
              }
    html = requests.get(url,headers=header)
    soup = BeautifulSoup(html.text, 'html.parser')
    songs=soup.select('div.ellipsis.rank01')
    #print(soup)
    #print(songs)

    song_list = [s.getText().strip("\n \t") for s in songs]
    #print(song_list)

    return song_list