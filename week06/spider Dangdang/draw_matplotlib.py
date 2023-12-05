import matplotlib.pyplot as plt
import numpy as np

# 创建随机数据集
x = np.linspace(0, 10, 100)
y1 = np.random.randn(100)
y2 = np.random.randn(100)
categories = ['A', 'B', 'C', 'D', 'E']
values = np.random.randint(0, 100, len(categories))

# 创建子图
fig, axs = plt.subplots(1, 3, figsize=(12, 4))

# 子图1：折线图
axs[0].plot(x, y1)
axs[0].set_title('Line Plot')

# 子图2：散点图
axs[1].scatter(x, y2)
axs[1].set_title('Scatter Plot')

# 子图3：柱状图
axs[2].bar(categories, values)
axs[2].set_title('Bar Plot')

# 调整子图之间的间距
plt.tight_layout()

# 显示图形
plt.show()