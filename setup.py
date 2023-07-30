
import pandas as pd

# 读取 Excel 文件
dataset = pd.read_excel('D://thesis relevant WD//final data//raw data to be worked.xlsx')

a = dataset.shape
print(a)

# 将除了第一列之外的所有的0和负数替换为 NaN
dataset.iloc[:, 1:] = dataset.iloc[:, 1:].mask(dataset.iloc[:, 1:] <= 0)

# 删除最后一列全部大于105的数据
dataset.iloc[:, -1] = dataset.iloc[:, -1].mask(dataset.iloc[:, -1] > 105)

# 遍历每一列（从第 8 列到第 35 列）
for column_index in range(8, 35):
    # 设置差异阈值
    diff_threshold = 4.5 \
        if column_index == 8 else 9

    # 清除与上方差别过大的数据
    for i in range(len(dataset) - 1):
        if abs(dataset.iloc[i, column_index] - dataset.iloc[i + 1, column_index]) > diff_threshold:
            dataset.iloc[i, column_index] = None

# 指定要检查的列范围（从 I 列到 AI 列）
column_range = dataset.columns[8:35]

# 删除全部为空的行
dataset.dropna(subset=column_range, how='all', inplace=True)

# 重置行索引
dataset.reset_index(drop=True, inplace=True)

# 导出为 Excel 文件
dataset.to_excel('output2.xlsx', index=False)  # index=False 表示不导出索引列
import pandas as pd

# 读取 Excel 文件
dataset = pd.read_excel('D://thesis relevant WD//final data//raw data to be worked.xlsx')

a = dataset.shape
print(a)

# 将除了第一列之外的所有的0和负数替换为 NaN
dataset.iloc[:, 1:] = dataset.iloc[:, 1:].mask(dataset.iloc[:, 1:] <= 0)

# 删除最后一列全部大于105的数据
dataset.iloc[:, -1] = dataset.iloc[:, -1].mask(dataset.iloc[:, -1] > 105)

# 遍历每一列（从第 8 列到第 35 列）
for column_index in range(8, 35):
    # 设置差异阈值
    diff_threshold = 4.5 \
        if column_index == 8 else 9

    # 清除与上方差别过大的数据
    for i in range(len(dataset) - 1):
        if abs(dataset.iloc[i, column_index] - dataset.iloc[i + 1, column_index]) > diff_threshold:
            dataset.iloc[i, column_index] = None

# 指定要检查的列范围（从 I 列到 AI 列）
column_range = dataset.columns[8:35]

# 删除全部为空的行
dataset.dropna(subset=column_range, how='all', inplace=True)

# 重置行索引
dataset.reset_index(drop=True, inplace=True)

# 导出为 Excel 文件
dataset.to_excel('output2.xlsx', index=False)