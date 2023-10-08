import random





def selection_sort(num_list):
    length = len(num_list)
    if length <= 1:
        return num_list
    for j in range(length):
        min_num_index = j
        for i in range(j + 1, length):
            if num_list[i] < num_list[min_num_index]:
                min_num_index = i
        num_list[min_num_index], num_list[j] = num_list[j], num_list[min_num_index]

    return num_list


def quick_sort(num_list):
    if len(num_list) >= 2:
        key = num_list[len(num_list) // 2]  # 选取基准值
        right, left = [], []  # 定义左右两侧数组
        num_list.remove(key)  # 从原数组中移除基准值
        for i in num_list:
            if i < key:
                left.append(i)
            else:
                right.append(i)
        return quick_sort(left) + [key] + quick_sort(right)
    else:
        return num_list


def print_list(x, num_list):
    print("第", x, "组：")
    for i in range(len(num_list)):
        print(num_list[i], end=" ")


if __name__ == "__main__":
    n = 0
    print("请输入要生成多少个随机数组：")
    n = int(input())
    num = [[]for _ in range(n)]
    num_quick = [[]for _ in range(n)]
    for i in range(0, n):
        for j in range(n-i-1, n):
            num[i].append(random.randint(1, 100))
    num_quick = num
    for i in range(n):
        selection_sort(num[i])
        quick_sort(num_quick[i])
    print("选择排序结果是：")
    for i in range(n):
        print_list(i, num[i])
        print("\n")
    print("快速排序结果是：")
    for i in range(n):
        print_list(i, num_quick[i])
        print("\n")