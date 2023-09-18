s = input("请输入要判断的字符串：")

count = 0


length = len(s) - 1

for i in range(length):
    if s[i] == s[i+1] :
        count += 1
    i += 1
if count != 0:
    print("其中包含两个或两个以上连续出现的字符")
else:
    print("其中不包括两个或两个以上连续出现的字符")


