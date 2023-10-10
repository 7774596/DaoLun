def insertSort(arr):
    for i in range(len(arr)):
        tmp = i-1
        current = arr[i]
        while tmp >=0 and arr[tmp] > current:
            arr[tmp+1] = arr[tmp]
            tmp -= 1
        arr[tmp+1] = current
    return arr

if __name__ == "__main__":
    print("请输入需要排序的数字序列：")
    arr=input().split()
    print(insertSort(arr))