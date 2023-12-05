import pandas as pd
import matplotlib.pyplot as plt

# 创建 DataFrame
df = pd.read_csv('SVMtrain.csv')

# 查看整体信息
df.info()

# 查看统计摘要
df.describe()

# 处理缺失值
numeric_columns = df.select_dtypes(include='number').columns
mean_values = df[numeric_columns].mean()                       # 计算所有数值列的均值
df[numeric_columns] = df[numeric_columns].fillna(mean_values)
column_mode = df['Sex'].mode()[0]                              # 使用均值填充缺失值

# 使用众数值填充Sex列缺失值
df['Sex'].fillna(column_mode, inplace=True)
df.drop_duplicates()  # 删除重复行

# 数据可视化
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

axes[0].hist(df['Age'])
axes[0].set_title('Age Histogram')   # 年龄统计直方图

sex_counts = df['Sex'].value_counts()
axes[1].pie(sex_counts, labels=sex_counts.index, autopct='%1.1f%%')  # 性别分布图
axes[1].set_title('Sex Pie Chart')

plt.tight_layout()
plt.show()


