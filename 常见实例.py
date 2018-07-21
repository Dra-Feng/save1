import re

#匹配.com或.cn后缀的URL网址
pattern1="[a-zA-Z]+://[^\s]*[.com|.cn]"
string1="href=http://www.baidu.com/img/baidu_85beaf5496f291521eb75ba38eacbd87.svg><title>百度一下，你就知道 </title>"
result1=re.search(pattern1, string1)
print(result1)

#匹配电话号码
pattern2="\d{4}-\d{7}|\d{3}-\d{8}"      #匹配电话号码的正则表达式
string2="021-6728282828282828828554"
result2=re.search(pattern2,string2)
print(result2)

#匹配电子邮件地址
pattern3="\w+([.+-]\w+)*@\w+([.-]\w+)*\.\w+([.-]\w+)*"      #匹配电子邮件的正则表达式
string3="<a herf='http://www.baidu.com'>百度首页</a><br><a href='mailto:c-e+o@iqianyue.com.cn'>电子邮件地址</a>"
result3=re.search(pattern3,string3)
print(result3)