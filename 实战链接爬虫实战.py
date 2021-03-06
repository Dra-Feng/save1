import re
import urllib.request
def getlink(url):
    #模拟成浏览器
    header=("User-Agent","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36")
    opener=urllib.request.build_opener()
    opener.addheaders=[header]
    #将opener安装为全局
    urllib.request.install_opener(opener)
    file=urllib.request.urlopen(url)
    data=str(file.read())
    #根据需求构建好链接表达式
    pat='(https?://[^\s)";]+\.(\w|/)*)'
    link=re.compile(pat).findall(data)
    #去重复元素
    link=list(set(link))
    return link

#要爬取的网页链接
url="http://blog.csdn.net/"
#获取对应网页中包含的链接地址
linklist=getlink(url)
#通过for循环分别遍历输出获取到的链接地址到屏幕上
for link in linklist:
    print(link[0])