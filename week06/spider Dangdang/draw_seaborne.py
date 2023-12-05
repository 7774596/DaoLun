import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 示例数据
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]
data = np.random.randn(1000)

# 创建子图
fig, axes = plt.subplots(1, 3, figsize=(12, 4))

# 绘制折线图
sns.lineplot(x=x, y=y1, ax=axes[0])
axes[0].set_title('Line Plot')

# 绘制散点图
sns.scatterplot(x=x, y=y2, ax=axes[1])
axes[1].set_title('Scatter Plot')

# 绘制直方图
sns.histplot(data=data, ax=axes[2])
axes[2].set_title('Histogram')

# 调整子图之间的间距
plt.tight_layout()

# 显示图形
plt.show()