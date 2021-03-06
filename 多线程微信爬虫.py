import threading
import queue
import re
import urllib.request
import time
import urllib.error

urlqueue=queue.Queue()
#模拟成浏览器
headers = ("User-Agent","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36")
opener=urllib.request.build_opener()
opener.addheaders=[headers]
#将opener安装为全局
urllib.request.install_opener(opener)
listurl=[]
#使用代理服务器的函数
def use_proxy(proxy_addr,url):
    try:
        proxy=urllib.request.ProxyHandler({'http':proxy_addr})
        opener=urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
        urllib.request.build_opener(opener)
        data=urllib.request.urlopen(url).read().decode("utf-8")
        return data
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
        time.sleep(10)
    except Exception as e:
        print("exception:"+str(e))
        time.sleep(1)

#线程1,专门获取对应网址并处理为真实网址
class geturl(threading.Thread):
    def __inint__(self,key,pagestart,pageend,proxy,urlqueue):
        threading.Thread.__init__(self)
        self.pagestart=pagestart
        self.pageend=pageend
        self.proxy=proxy
        self.urlqueue=urlqueue
        self.key=key
    def run(self):
        page=self