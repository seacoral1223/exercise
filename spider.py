import requests
from bs4 import BeautifulSoup

res = requests.get("https://www.runoob.com/cplusplus/cpp-tutorial.html")

if res.status_code == 200:
    data = res.text
    soup = BeautifulSoup(data, "lxml")
    print(soup.h1.string)
else:
    print("请求失败")