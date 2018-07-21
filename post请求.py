import urllib.request
import urllib.parse

url="http://www.iqianyue.com/mypost"
postdata=urllib.parse.urlencode({
    "name":"ceo@iqianyue.com",
    "pass":"123456"
}).encode('utf-8') #将数据使用urlencode编码处理后，使用encode()设置为utf-8编码
req=urllib.request.Request(url,postdata)
req.add_header('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36')
data=urllib.request.urlopen(req).read()
fhandle=open("/home/liu/6.html","wb")
fhandle.write(data)
fhandle.close()