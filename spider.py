import requests
from bs4 import BeautifulSoup

res = requests.get("https://www.cnblogs.com/minuhy/p/18686886")

if res.status_code == 200:
    data = res.text
    soup = BeautifulSoup(data, "lxml")
    print(soup.h1.string)
else:
    print("请求失败")