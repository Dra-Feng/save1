import urllib.request

file=urllib.request.urlopen("http://blog.csdn.net/weiwei_pig/article/details/51178226")
data=file.read()
dataline=file.readline()
print(dataline)
fhandle=open("/home/liu/3.html","wb")
fhandle.write(data)
fhandle.close()