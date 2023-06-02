import requests
import sys
import py_utils as u

# 开奖数据文件路径
path_asc = './Data/ssq_asc.txt'


def request_data():
    """请求更新数据并保存到本地（覆盖原有数据）
    """

    u.debug_print('开始请求数据...')
    url = 'http://data.17500.cn/ssq_asc.txt'

    # 设置请求头
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.50'
    }

    # 发送请求
    rs = requests.get(url=url, headers=headers)

    # 判断请求是否成功 200表示成功 404表示失败 403表示禁止访问 500表示服务器错误 502表示网关错误 503表示服务不可用 504表示网关超时
    if rs.status_code == 200:
        # 保存数据到本地(覆盖原有数据)，文件名：ssq_asc.txt
        with open(path_asc, 'wb') as f:
            f.write(rs.content)
        u.debug_print('更新数据更新成功...')
    else:
        u.debug_print('更新数据更新失败, 请检查网络链接!')
        sys.exit(1)  # 退出程序
