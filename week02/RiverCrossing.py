

# 起始时全在河这边
# 0人 1狼 2羊 3菜


# status = []
'''

def judge_finish():
    if itom[0] + itom[1] + itom[2] + itom[3] == 4:
        return False
    else:
        return True

# 羊要么单独在一边要么跟人在一块

def judge():
    if (itom[2] == itom[0]) or (itom[2] != itom[3] and itom[2] != itom[1]):
        return True
    else:
        return False

def set_status(status):
    status[0] = itom[0]
    status[1] = itom[1]
    status[2] = itom[2]
    status[3] = itom[3]

def create_history():
    global count
    history_status.append(status.copy())

# 0人啥也不带 1人带狼 2人带菜 3人带菜

# 农夫过河带第i个物品
def same():
    if status in history_status:
        return False
    return True


def check_status(status):
    if (status[2] == status[0]) or (status[2] != status[3] and status[2] != status[1]):
        return True
    else:
        return False


def cross_river(i): # 当前能否带i渡河
    global count
    if itom[0] == itom[i]:
        itom[0] = itom[i] = not itom[0]
        set_status()
    return status


def deep_search(history_status):
    while judge_finish():
        for i in range(4):
            cross_river(i)



if __name__ == "__main__":
    count = 0
    status = [0, 0, 0, 0]
    itom = [0, 0, 0, 0]
    history_status = []
    create_history()
    while judge_finish():
        for i in range(4):
            cross_river(i)
    for j in range(count):
        for i in range(4):
            print(history_status[j][i], end=" ")
        print("\n")
'''

ways = 0


# 完成局面
def judge_finish(status):
    return status[0] and status[1] and status[2] and status[3]


# 生成下一个局面的所有情况
def create_next_status(status):
    next_status_list = []
    for i in range(4):
        if status[0] != status[i]: # 和农夫不同一侧？
            continue
        next_status = [status[0], status[1], status[2], status[3]]
        next_status[0] = 1 - next_status[0]
        next_status[i] = next_status[0]
        if check_status(next_status):
            next_status_list.append(next_status)
    return next_status_list


# 判断是否合法的局面
def check_status(status):
    if (status[2] == status[0]) or (status[2] != status[3] and status[2] != status[1]):
        return True
    else:
        return False


def search(history_status):
    # 定义全局变量
    global ways
    current_status = history_status[len(history_status) - 1]
    next_status_list = create_next_status(current_status)
    for next_status in next_status_list:
        if next_status in history_status:
            continue
        history_status.append(next_status)
        if judge_finish(next_status):
            ways += 1
            print("way" + str(ways) + ":")
            print_history_status(history_status)
        else:
            search(history_status)
        history_status.pop() # 回退直到回退到正确的分支节点


def print_history_status(history_status):
    for i in range(len(history_status)):
        print(history_status[i])


if __name__ == "__main__":
    status = [0, 0, 0, 0]
    history_status = [status]
    search(history_status)













