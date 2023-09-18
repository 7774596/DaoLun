seq = input("请输入要重新排序的序列:");
length = len(seq) - 1
for i in range(len(seq) - 1, -1, -1):
    print(seq[i],end=" ")
print("\n")


llength = length
while llength >= 0:
    print(seq[llength], end=" ")
    llength -= 1