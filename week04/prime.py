
def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


if __name__ == "__main__":

    num = int(input("请输入一个整数："))
    if is_prime(num):
        print(f"{num} 是质数")
    else:
        print(f"{num} 不是质数")

