# from pyecharts.charts import Bar
# from pyecharts import options as opts

# # V1 版本开始支持链式调用
# bar = (
#     Bar()
#     .add_xaxis(["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"])
#     .add_yaxis("商家A", [114, 55, 27, 101, 125, 27, 105])
#     .add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])
#     .set_global_opts(title_opts=opts.TitleOpts(title="某商场销售情况"))
# )
# bar.render()

# # 不习惯链式调用的开发者依旧可以单独调用方法
# bar = Bar()
# bar.add_xaxis(["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"])
# bar.add_yaxis("商家A", [114, 55, 27, 101, 125, 27, 105])
# bar.add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])
# bar.set_global_opts(title_opts=opts.TitleOpts(title="某商场销售情况"))
# bar.render()

# import pyecharts

# print(pyecharts.__version__)

# import pandas as pd

# data = [[ 66386, 174296,  75131, 577908,  32015],
#         [ 58230, 381139,  78045,  99308, 160454],
#         [ 89135,  80552, 152558, 497981, 603535],
#         [ 78415,  81858, 150656, 193263,  69638],
#         [139361, 331509, 343164, 781380,  52269]]
# columns=('Freeze', 'Wind', 'Flood', 'Quake', 'Hail')

# rows = ['%d year'% x for x in (100, 50, 20, 10, 5)]
# df = pd.DataFrame(data, columns=('Freeze', 'Wind', 'Flood', 'Quake', 'Hail'),
#                   index=rows)
# print(df)

# # coding:utf-8
# from pyecharts.charts import Bar, Page
# from pyecharts import options as opts
# import os
# if __name__ == '__main__':
#     # pyecharts=1.8.1
#     # 安装 python -m pip install pyecharts
#     page = Page(layout=Page.DraggablePageLayout)
#     bar = Bar()
#     bar.add_xaxis(["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"])
#     bar.add_yaxis("商家A", [114, 55, 27, 101, 125, 27, 105])
#     bar.add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])
#     bar.add_yaxis("商家C", [57, 134, 137, 129, 145, 60, 49])
#     bar.set_global_opts(title_opts=opts.TitleOpts(title="某商场销售情况1"))
#     bar1 = Bar()
#     bar1.add_xaxis(["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"])
#     bar1.add_yaxis("商家A", [114, 55, 27, 101, 125, 27, 105])
#     bar1.add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])
#     bar1.add_yaxis("商家C", [57, 134, 137, 129, 145, 60, 49])
#     bar1.set_global_opts(title_opts=opts.TitleOpts(title="某商场销售情况2"))
#     # 将柱状图bar和bar1添加到page页面中，这样就可以将两个图标绘制成一个html中了

#     page.add(bar, bar1)
#     page.render("test.html")
#     os.system("test.html")

# import itertools

# # 所有组合数17721088

# # 生成1到34的数字列表
# numbers = list(range(1, 34))

# # 计算排列组合

# combos = itertools.combinations(numbers, 6)
# i = 0
# # 1-33 的数字中，任取6个数字的排列组合数为：C(33,6) = 33! / (6! * (33-6)!) = 5,005,520
# # 将计算记过保存到txt文本中
# with open('combos.txt', 'w') as f:
#     for combo in combos:
#         f.write(','.join(str(num) for num in combo) + '\n')
# print('Done!')

# import os
# from collections import Counter
# from tabulate import tabulate

# # 统计数据个数

# # 指定要切割的行数
# row_size = 50

# # 读取数据(开奖信息) 格式为二维List red1,red2,red3,red4,red5,red6,blue
# data_lottery = []
# with open('Others\Python\SSQ\ssq_asc.txt', 'r') as f:
#     for line in f:
#         fields = line.strip().split()[2:9]
#         data_lottery.append(fields)

# data_rows = []
# result = []
# # 将数据切割为指定行数
# for i in range(0, len(data_lottery), row_size):
#     rows = data_lottery[i:i + row_size]

#     # 将数据转换成1维列表
#     data_rows = [element for sublist in rows for element in sublist]

#     # 统计数据出现次数
#     rows_counter = Counter(data_rows)

#     # 将Counter中的键按整数类型排序
#     sorted_keys = sorted(map(int, rows_counter.keys()))

#     # 创建一个新的Counter对象，并为缺失的键添加键值对
#     new_counter = Counter({f'{k:02d}': 0 for k in range(1, 34)})
#     new_counter.update(rows_counter)

#     # 将新的Counter对象中的键按照排好序的键列表进行排序
#     sorted_output = Counter({f'{k:02d}': new_counter[f'{k:02d}'] for k in sorted_keys})

#     # 将结果字典保存到result里
#     result.append(dict(sorted_output))

# # 转换字典为列表
# rows = [[r[k] for k in sorted(r.keys())] for r in result]

# # 打印表格
# print(tabulate(rows, headers=[f'red {k}' for k in range(1, 34)]))