
import pandas as pd

# 读取 Parquet 文件
df = pd.read_parquet('mix_cl_a50.parquet')

# 打开一个 txt 文件进行写入
with open('output.txt', 'w') as f:
    # 遍历 DataFrame 的每一行，将每一行数据按列写入文本文件
    for index, row in df.iterrows():
        # 将每一行的列数据转换为字符串，并用逗号分隔
        line = ', '.join(map(str, row))  # 你可以根据需要选择分隔符，比如逗号、制表符等
        f.write(line + '\n')  # 写入行，并在末尾添加换行符
