import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)

res.raise_for_status()

soup = BeautifulSoup(res.text , "lxml")
print(soup.title)
print(soup.title.get_text())

# print(soup.a) # 첫번째 a를 가지고와라 
# print(soup.a.attrs) # a태그의 속성
# print(soup.a["href"]) # a속성의 특정값 호출

# print(soup.find("a" ,attrs={"class" : "Nbtn_upload"} ))
 
# print(rank1.a)
# print(rank1.a.get_text())
# print(rank1.next_sibling.next_sibling)
rank1 = soup.find("li", attrs={"class" : "rank01"})
#print(rank1.find_next_siblings("li"))

webtoon = soup.find("a",text="가")
print(webtoon)