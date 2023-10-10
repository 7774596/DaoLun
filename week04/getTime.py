import time
import re
# 记录开始时间

print("请输入一个身份证号：")
st = input()
start_time = time.time()
if re.match(r'(^\d{15}$)|(^\d{17}([0-9]|x)$)', st):
    print("这是一个合法的身份证号")
else:
    print("这不是一个合法的身份证号")


end_time = time.time()

# 计算程序执行时间
execution_time = end_time - start_time

print(f"程序执行时间：{execution_time} 秒")
