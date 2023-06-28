import py_utils as u
from itertools import combinations, product
import time
from tqdm import tqdm


def make_all_combos():
    """生成所有的组合
    """
    u.debug_print('开始生成所有的组合...')
    reds = range(1, 33+1)
    blues = range(1, 16+1)

    combos = list(product(combinations(reds, 6), combinations(blues, 1)))
    result = [','.join(map(str, elem[0])) + ',' + str(elem[1][0]) for elem in combos]

    with tqdm(total=17721088, desc='all_combos', leave=True, ncols=100) as pbar:
        # 将combos 打印到文件中
        with open('./Data/all_combos.txt', 'w') as f:
            for c in result:
                f.write(c + '\n')
                pbar.update(1)
    u.debug_print('生成所有的组合成功...')


# 生成红球所有组合
def make_red_combos():
    """生成红球所有组合
    """
    u.debug_print('开始生成红球所有组合...')
    reds = range(1, 33+1)
    combos = list(combinations(reds, 6))
    result = [','.join(map(str, elem)) for elem in combos]

    with tqdm(total=1107569, desc='red_combos', leave=True, ncols=100) as pbar:
        # 将combos 打印到文件中
        with open('./Data/red_combos.txt', 'w') as f:
            for c in result:
                f.write(c + '\n')
                pbar.update(1)
    u.debug_print('生成红球所有组合成功...')
