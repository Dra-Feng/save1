#http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=LtES6
import urllib.request
import urllib.parse
import http.cookiejar

url="http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=Lqwp4"
postdata=urllib.parse.urlencode({
    "username":"Stitch丶",
    "password":"nihao963852"
}).encode('utf-8')
req=urllib.request.Request(url,postdata)
req.add_header('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36')
#使用http.cookiejar.CookieJar()创建CookieJar对象
cjar=http.cookiejar.CookieJar()
#使用HTTPCookieProcessor创建 cooie处理器,并以其为参数构建opener对象
opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
#将opener安装为全局
urllib.request.install_opener(opener)
file=opener.open(req)
data=file.read()
file=open("/home/liu/cookaaa.html","wb")
file.write(data)
file.close()
url2="http://bbs.chinaunix.net/"
data2=urllib.request.urlopen(url2).read()
fhandle=open("/home/liu/cookbbb.html","wb")
fhandle.write(data2)
fhandle.close()