import urllib.request

url="http://www.baidu.com"
req=urllib.request.Request(url)
req.add_header('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36')
data=urllib.request.urlopen(req).read()
print(data)