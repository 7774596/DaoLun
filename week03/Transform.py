print("请输入需要转换的十进制数字：")

num = float(input())

#print("其二进制表示为:", bin(num).lstrip("0b"))

left = num - int(num)

left_binary = ""
tmp = float(0)

while left == left - int(left) and left != 0:
    left = left*2
    bin_num = int(left)
    left_binary += str(bin_num)
    if bin_num != 0:
        left = left - int(left)
    if len(left_binary) >= 10:
        break

print("这个数的二进制表示是:", bin(int(num)).lstrip("0b")+"."+left_binary)




