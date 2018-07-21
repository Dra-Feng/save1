import urllib.request

keywd="微微"
key_code=urllib.request.quote(keywd)
url="http://www.baidu.com/s?wd="+key_code  #中文字符会出现问题，加quote进行编码
req=urllib.request.Request(url)
data=urllib.request.urlopen(req).read()
fhandle=open("/home/liu/5.html","wb")
fhandle.write(data)
fhandle.close()

