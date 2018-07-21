import urllib.request
import http.cookiejar
#注意,如果要通过fiddler调试,则下方网址要设置为"http://www.baidu.com/" (以/结尾)
url="http://www.baidu.com"
headers={"Accept":"text/html,application/xhtml,application/xml;q=0.9,*/*;q=0.8",
         "Accept-Encoding":"gb2312,utf-8",
         "Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
         "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
         "Connection":"keep-alive",
         "referer":"baidu.com"}
cjar=http.cookiejar.CookieJar()
opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
headall=[]
for key,value in headers.items():
    item=(key,value)
    headall.append(item)
opener.addheaders=headall
urllib.request.install_opener(opener)
data=urllib.request.urlopen(url).read()
fhandle=open("/home/liu/爬虫实战初体验/伪装技术/伪装技术3.html","wb")
fhandle.write(data)
fhandle.close()