import pandas as pd
import py_utils as u
import py_request as req


u.debug_print('程序开始运行...')

# 更新开奖数据
req.request_data()


# 是否指定年份数据
while True:
    is_year = input('是否指定年份数据？(y/n): ')
    if is_year.lower() not in ['y', 'n']:
        u.debug_print('输入错误：请输入 y 或 n !')
    else:
        year = None
        break

# 验证年份数据
if is_year == 'y':
    year = input('请输入年份(yyyy): ')
    while True:
        if year.isdigit() and len(year) == 4:
            break
        else:
            u.debug_print('输入错误：请输入正确的年份(yyyy)!')

# 是否指定期数
while True:
    is_row = input('是否指定期数？(y/n): ')
    if is_row.lower() not in ['y', 'n']:
        u.debug_print('输入错误：请输入 y 或 n !')
    else:
        row_size = None
        break

# 验证期数
if is_row == 'y':
    row_size = input('请输入期数,至少请填写5期及以上: ')
    while True:
        if row_size.isdigit() and int(row_size) >= 5:
            break
        else:
            u.debug_print('输入错误或期数过少：请输入正确的期数!')

# 读取开奖数据
data = u.get_latest_lottery_results(year=year, rows=row_size)

# 计算红球和值
data = u.calc_sum_red_balls(data)

# 计算红球横向差值偏移量
data = u.calc_offset_red_balls(data)

# 计算红球差值偏移量和值
data = u.calc_sum_offset_red_balls(data)

# 计算红球竖向差值偏移量
data = u.calc_vertical_offset_red_balls(data)

# 计算红球竖向差值偏移量和值
data = u.calc_sum_vertical_offset_red_balls(data)

# 计算连号
data = u.calc_continuous_number_red_balls(data)

# 打印分析结果到Excel
u.print_to_excel('原始数据', data)

# 生成走势图
new_data = u.generate_trend_chart(data)
u.print_to_excel('走势图', new_data)


u.debug_print('分析完毕...')