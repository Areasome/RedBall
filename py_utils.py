import datetime
import pandas as pd

path_asc = './Data/ssq_asc.txt'


def debug_print(message):
    """打印带时间戳的调试信息到控制台
    Args:
        message (字符串): 调试信息
    """

    # 获取当前时间
    current_time = datetime.datetime.now()
    # 格式化时间戳字符串
    timestamp_str = current_time.strftime('[%Y-%m-%d %H:%M:%S]')
    # 打印带时间戳的调试信息
    print(f'[Info]{timestamp_str} {message}')


def get_latest_lottery_results(year, rows):
    """读取开建该数据

    Args:
        year (int): 开奖年份
        rows (int): 开奖数据行

    Returns:
        list: 返回开奖数据前9列
              分别为 ->> 期号、开奖日期、红球1、红球2、红球3、红球4、红球5、红球6、蓝球
    """

    # 筛选期数符合年份的开奖数据
    with open(path_asc, 'r') as f:
        data_lottery = []
        # 指定年份
        if year != None:
            for line in f:
                fields = line.strip().split()[:9]
                if fields[0].startswith(year):
                    data_lottery.append(fields)
        # 不指定年份
        else:
            for line in f:
                fields = line.strip().split()[:9]
                data_lottery.append(fields)

    # 返回指定行数的数据
    if rows != None:
        if rows > len(data_lottery):
            rows = len(data_lottery)
        data_lottery = data_lottery[-rows:]

    # 返回开奖数据
    return data_lottery


def calc_sum_red_balls(data_lottery):
    """计算红球和值

    Args:
        data_lottery (list): 开奖数据

    Returns:
        list: 追加开奖数据和值列(共1列)
    """

    # 计算红球和值
    debug_print('计算红球和值...')
    for i in range(len(data_lottery)):
        data_lottery[i].append(str(sum([int(x) for x in data_lottery[i][2:8]])))

    # 返回开奖数据
    return data_lottery


def calc_offset_red_balls(data_lottery):
    """计算红球横向差值偏移量

    Args:
        data_lottery (list): 开奖数据

    Returns:
        list: 追加开奖数据红球横向差值偏移量列(共5列)
    """

    # 计算每个红球横向差值偏移量
    debug_print('计算红球横向差值偏移量...')
    for i in range(len(data_lottery)):
        data_lottery[i].append(str(int(data_lottery[i][3]) - int(data_lottery[i][2])))
        data_lottery[i].append(str(int(data_lottery[i][4]) - int(data_lottery[i][3])))
        data_lottery[i].append(str(int(data_lottery[i][5]) - int(data_lottery[i][4])))
        data_lottery[i].append(str(int(data_lottery[i][6]) - int(data_lottery[i][5])))
        data_lottery[i].append(str(int(data_lottery[i][7]) - int(data_lottery[i][6])))

    # 返回开奖数据
    return data_lottery


def calc_sum_offset_red_balls(data_lottery):
    """计算红球横向差值偏移量和值

    Args:
        data_lottery (list): 开奖数据

    Returns:
        list: 追加开奖数据红球横向差值偏移量和值列(共1列)
    """

    # 计算红球横向差值偏移量和值
    debug_print('计算红球横向差值偏移量和值...')
    for i in range(len(data_lottery)):
        data_lottery[i].append(str(sum([int(x) for x in data_lottery[i][10:15]])))

    # 返回开奖数据
    return data_lottery


def calc_vertical_offset_red_balls(data_lottery):
    """计算红球纵向差值偏移量

    Args:
        data_lottery (list): 开奖数据

    Returns:
        list: 追加开奖数据红球纵向差值偏移量列(共6列)
    """

    # 计算每个红球纵向差值偏移量
    debug_print('计算红球纵向差值偏移量...')
    for i in range(len(data_lottery)):
        for j in range(2, 8):
            if i == 0:
                data_lottery[i].append('0')
            else:
                data_lottery[i].append(str(int(data_lottery[i][j]) - int(data_lottery[i-1][j])))

    # 返回开奖数据
    return data_lottery


def calc_sum_vertical_offset_red_balls(data_lottery):
    """计算红球纵向差值偏移量和值

    Args:
        data_lottery (list): 开奖数据

    Returns:
        list: 追加开奖数据红球纵向差值偏移量和值列(共1列)
    """

    # 计算红球纵向差值偏移量和值
    debug_print('计算红球纵向差值偏移量和值...')
    for i in range(len(data_lottery)):
        data_lottery[i].append(str(sum([int(x) for x in data_lottery[i][16:22]])))

    # 返回开奖数据
    return data_lottery


def calc_continuous_number_red_balls(data_lottery):
    """计算红球连号出现的次数

    Args:
        data_lottery (list): 开奖数据

    Returns:
        list: 追加开奖数据连号出现的次数列(共1列)
    """

    # 计算连号出现的次数
    debug_print('计算连号出现的次数...')
    num = 0
    for i in range(len(data_lottery)):
        for j in range(2, 7):
            if int(data_lottery[i][j]) - int(data_lottery[i][j+1]) == -1:
                num += 1

        data_lottery[i].append(str(num))
        num = 0

    # 返回开奖数据
    return data_lottery


def generate_trend_chart(data_lottery):
    """生成双色球红球1-33和篮球1-16的走势图,并计算每个号码的遗漏值

    Args:
        data_lottery (list): 开奖数据

    Returns:
        list: 追加开奖数据红球1-33和篮球1-16的走势图列(共49列)
    """

    # 生成双色球红球1-33和篮球1-16的走势图
    debug_print('生成双色球红球1-33和篮球1-16的走势图...')
    new_data_lottery = [[] for i in range(len(data_lottery))]
    for i in range(len(data_lottery)):
        for j in range(0, 33):
            if str(j) in data_lottery[i][2:8]:
                new_data_lottery[i].append(str(j))
            else:
                new_data_lottery[i].append('0')

        for j in range(0, 16):
            if str(j) in data_lottery[i][8]:
                new_data_lottery[i].append(str(j))

            else:
                new_data_lottery[i].append('0')

    # 返回开奖数据
    return new_data_lottery


def print_to_excel(sheet, data_lottery):
    """输出结果到Excel

    Args:
        sheet (str): sheet名称
        data (list): 数据源
    """

    debug_print('输出结果到文件...')
    headers = ('期号,开奖日期,红球1,红球2,红球3,红球4,红球5,红球6,蓝球,红球和值,'
               '红球1偏移(横),红球2偏移(横),红球3偏移(横),红球4偏移(横),红球5偏移(横),红球偏移和值(横),'
               '红球1偏移(竖),红球2偏移(竖),红球3偏移(竖),红球4偏移(竖),红球5偏移(竖),红球6偏移(竖),红球偏移和值(竖),'
               '连号次数').split(',')

    # 创建DataFrame对象
    df = pd.DataFrame(data_lottery, columns=headers)

    # 将第1列转换为整数类型
    df.iloc[:, 0] = df.iloc[:, 0].astype(int)

    # 将第2列以后的所有数据转换为整数类型
    df.iloc[:, 2:] = df.iloc[:, 2:].astype(int)

    df.to_excel('./Data/output.xlsx', sheet_name=sheet, index=False, header=True)
    debug_print('分析完成!')

# def analyze_lottery_results():
