import re
pattern1="p.*y"     #贪婪模式
pattern2="p.*?y"    #懒惰模式
string="abcdefphp345pythony_py"
result=re.search(pattern1,string)
result2=re.search(pattern2,string)
print(result)
print(result2)

#贪婪模式：一直搜索直到最后一个结尾字符y
#懒惰模式：找到第一个结尾字符y就停止搜索