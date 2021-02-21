import requests
url = ""http://nadocoding.tistory.com"
headers = {"User-Agent" : "@@@@"}
res = requests.get(url,headers)

with open("nadocoding.html" , "w" , encoding="utf8") as f:
    f.write(res.text)