import py_utils as u
import itertools
import pandas as pd

s_rows = -4

# 读取output Excel Raw Data sheet第二列倒数5行的数据的数据
df = pd.read_excel('./Data/output.xlsx', sheet_name='Raw Data')
operators = ['+', '-', '*', '/']
output_list = []

for i in range(2, 9):
    # 从第二列开始获取数据

    # red 01
    if i == 2:
        e_rows = s_rows - 5
        
    # red 02
    if i == 3:
        e_rows = s_rows - 5
    
    # red 03
    if i == 4:
        e_rows = s_rows - 6
    
    # red 04
    if i == 5:
        e_rows = s_rows - 8
        
    # red 05
    if i == 6:
        e_rows = s_rows - 7
        
    # red 06
    if i == 7:
        e_rows = s_rows - 6
        
    # blue 01
    if i == 8:
        e_rows = s_rows - 5

    numbers = df.iloc[s_rows:(e_rows):-1, i].tolist()
    permutations = list(itertools.permutations(numbers))

    for permutation in permutations:
        for operator1 in operators:
            for operator2 in operators:
                expression = f"({permutation[0]} {operator1} {permutation[1]}) {operator2} {permutation[2]}"
                result = eval(expression)
                if i != 8:
                    if isinstance(result, int) and result > 0 and result % 1 == 0 and result <= 33:
                        output_list.append([expression, result])
                elif isinstance(result, int) and result > 0 and result % 1 == 0 and result <= 16:
                    output_list.append([expression, result])

    # output_list按第二列从小到大排序
    output_list.sort(key=lambda x: x[1])

    # 将结果保存到excel,保留原始sheet
    df_output = pd.DataFrame(output_list, columns=['operators', 'result'])
    # 分类汇总
    df_output['groupby'] = df_output.groupby('result')['result'].transform('size')
    # 删除重复数据
    df_output = df_output.drop_duplicates(subset=['result'])

    # 保存到excel
    with pd.ExcelWriter('./Data/output.xlsx', mode='a') as writer:
        try:
            writer.book.remove(writer.book[f'0{i-1}'])
        except:
            pass
        df_output.to_excel(writer, sheet_name=f'0{i-1}', index=False)

    # 清空list
    output_list = []
