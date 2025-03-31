import pandas as pd
import json

def excel_to_json(excel_file):
    # 读取Excel文件
    df = pd.read_excel(excel_file, header=None, names=['userName', 'userAvatar', 'comment']).iloc[1:]

    # 创建一个空列表来存储结果
    result = []

    # 遍历每一行数据
    for _, row in df.iterrows():
        user_data = {
            "userName": row['userName'],
            "userAvatar": row['userAvatar'],
            "comment": row['comment']
        }
        result.append(user_data)

    # 转换为JSON格式
    return json.dumps(result, ensure_ascii=False, indent=4)

# 指定你的Excel文件路径及名称
excel_file = '/Users/wuhaolei/work/python/teacher.xlsx'

# 生成JSON输出
json_output = excel_to_json(excel_file)
print(json_output)
