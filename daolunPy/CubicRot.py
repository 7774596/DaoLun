
num = float(input("请输入需要开三次方根的数字："))

def judge(x):
    if float(x*x*x) < num:
        return 1
    else:
        return 0


l = float(0)
r = num
if num < 0:
    l, r = r, l

while abs(r - l) > 1e-8:
    mid = (l + r)/2
    if judge(mid):
        l = mid
    else:
        r = mid

print("三次方根近似计算值是：", r)



