import re
pattern="python."
string="hellopythonhistoryourpythonendpythonm"
result=re.sub(pattern,"php",string)     #全部替换
result2=re.sub(pattern,"php",string,2)      #最多替换两次
print(result)
print(result2)
