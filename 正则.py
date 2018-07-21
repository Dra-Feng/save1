import re
pattern="^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$"
string="a@--.-_-"
result=re.search(pattern,string)
print(result)