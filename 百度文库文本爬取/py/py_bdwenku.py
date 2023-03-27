import requests
import bs4
from bs4 import BeautifulSoup
def getHTMLText(url):
    header = {'User-agent': 'Baiduspider'}#这句非常重要,不加爬不到,非得用百度的爬虫名字
    try:
        r = requests.get(url,headers = header, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding  #这句转码就不必要了,转成gb2312后会出现乱码,还是采用gbk的编码
        return r.text
    except:
        print("404")
        return ''

def getTXT(text):
    soup = BeautifulSoup(text,'html.parser')
    txt = ''
    for st in soup.find_all('div',style="border:1px solid #C8DBD3;padding:20px;line-height:24px;"):#只要文档那一截
    # for st in soup.find_all('div'):#
        txt += st.get_text()
    # print(txt)
    return txt

def my_Get(url):
    return getTXT(getHTMLText(url))


# url = 'https://wenku.baidu.com/view/227721723069a45177232f60ddccda38376be1d0.html?fr=aladdin664466&ind=1'
# url = 'https://wenku.baidu.com/view/5a3e0b636394dd88d0d233d4b14e852459fb3924.html'
# url = 'https://wenku.baidu.com/view/7010c996e97101f69e3143323968011ca300f7b6.html'

# url=input('请输入地址：')
# my_Get(url)