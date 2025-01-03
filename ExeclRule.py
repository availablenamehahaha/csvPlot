import pandas as pd

# 读取Excel文件
df = pd.read_excel('example.xlsx', engine='openpyxl')

print(df.head())

# 获取行数和列数
num_rows = len(df)
num_cols = len(df.columns)

print(f'行数: {num_rows}')
print(f'列数: {num_cols}')

rule = []

for index, row in df.iterrows():
    for col_name, value in row.items():
        print(f'  {col_name}: {value}')

    print()  # 空行用于分隔不同的行输出
