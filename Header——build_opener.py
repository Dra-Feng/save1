import urllib.request

url="http://www.baidu.com"
headers=("User-Agent"," Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36")
opener=urllib.request.build_opener()
opener.addheaders=[headers]
data=opener.open(url).read()
print(data)
fhandle=open("/home/liu/4.html","wb")
fhandle.write(data)
fhandle.close()