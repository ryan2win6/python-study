import requests
from bs4  import BeautifulSoup

url = "https://comic.naver.com/webtoon/list.nhn?titleId=703846&weekday=tue"

res = requests.get(url)
res.raise_for_status()

soup  = BeautifulSoup(res.text , "lxml")
cartoons = soup.find_all("td", attrs={"class":"title"})

title = cartoons[0].a.get_text()
link = cartoons[0].a["href"]

for cartoon in cartoons:
    titles = cartoon.a.get_text()
    links = cartoon.a["href"]

    print(titles)
    print(links)