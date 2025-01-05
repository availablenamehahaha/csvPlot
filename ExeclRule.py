import pandas as pd
import re
from main import transRule

patternDict = {'Name': r".*", 'PLOT': r"^[0-3]$", 'Color': r"^[r,g,b,y,c,m,k,w]$", 'ID': r"^[0-9a-fA-F]{1,8}$",
               'First': r"^(?:0|[1-9]|[1-5]\d|6[0-3])$", 'Bits': r"^(?:0|[1-9]|[1-5]\d|6[0-3])$",
               'Signed': r"^[0-1]$", 'Pu': r"^-?\d+(\.\d+)?$", 'Offset': r"^-?\d+(\.\d+)?$", 'intel': r"^[0-1]$"}

titleList = ['Name', 'ID', 'PLOT', 'Color', 'First', 'Bits', 'Signed', 'Pu', 'Offset', 'intel']


def ruleListAdd(df):
    ruleList = []
    # 读取Excel文件
    # print(df.head())
    # 获取行数和列数
    num_rows = len(df)
    num_cols = len(df.columns)
    print(f'行数: {num_rows}')
    print(f'列数: {num_cols}')
    headers = df.columns.tolist()
    print(f'表头{headers}')
    for head in headers:
        if head not in titleList:
            print(head)
            return None
    for index, row in df.iterrows():
        ruleTemp = transRule("")
        for col_name, value in row.items():
            # print(f'  {col_name}: {value}')
            if col_name == 'Name':
                match = re.match(patternDict.get(col_name), str(value))
                if match:
                    ruleTemp.name = value
            elif col_name == 'ID':
                match = re.match(patternDict.get(col_name), str(value))
                if match:
                    ruleTemp.ID = value
            elif col_name == 'First':
                match = re.match(patternDict.get(col_name), str(value))
                if match:
                    ruleTemp.begin = value
            elif col_name == 'Bits':
                match = re.match(patternDict.get(col_name), str(value))
                if match:
                    ruleTemp.bits = value
            elif col_name == 'Signed':
                match = re.match(patternDict.get(col_name), str(value))
                if match:
                    ruleTemp.signed = bool(value)
            elif col_name == 'Pu':
                match = re.match(patternDict.get(col_name), str(value))
                if match:
                    ruleTemp.pu = value
            elif col_name == 'Offset':
                match = re.match(patternDict.get(col_name), str(value))
                if match:
                    ruleTemp.offset = value
            elif col_name == 'intel':
                match = re.match(patternDict.get(col_name), str(value))
                if match:
                    ruleTemp.intel = bool(value)
            elif col_name == 'Color':
                match = re.match(patternDict.get(col_name), str(value))
                if match:
                    ruleTemp.color = value
        ruleList.append(ruleTemp)
        # print()  # 空行用于分隔不同的行输出
    print(f'解析规则行数:{len(ruleList)}')
    # for i in ruleList:
    #     print(i)
    return ruleList
