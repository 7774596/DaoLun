print(
    "60分以下不合格：F",
    "60-74分合格：C",
    "75-89分良好：B",
    "90-100分优秀：A",
)

print("请输入您的成绩：")
grade = int(input())
if grade in range(60):
    print("您的成绩是：", "F")
if grade in range(60, 75):
    print("您的成绩是：", "C")
if grade in range(75, 90):
    print("您的成绩是：", "B")
if grade in range(90, 101):
    print("您的成绩是：", "A")