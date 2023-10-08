import re

print("请输入一个身份证号：")
st = input()
if re.match(r'(^\d{15}$)|(^\d{17}([0-9]|x)$)', st):
    print("这是一个合法的身份证号")
else:
    print("这不是一个合法的身份证号")



