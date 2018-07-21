import re
string="apythonsdfspythonsdfpython99"
pattern=".python."
result1=re.compile(pattern).findall(string)
result2=re.match(pattern,string)
print(result1)
print(result2)