# import py_utils as u
import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime, timedelta
import pandas as pd

month_id = 41579

# 将 month id 转换为日期格式
# month_id_string = datetime(1900, 1, 1) + timedelta(days=month_id - 2)

# 齐天大圣,超人,青青草原
media_id = {"齐天大圣": 157, "超人": 215, "青青草原": 220}

# url = f"https://lts.zhcw.com/zhcw_leitaisai_front//jsp/leitai.jsp?mediaId={media_id}&monthId={month_id}&utilType=3"
url = f"https://lts.zhcw.com/zhcw_leitaisai_front//jsp/leitai.jsp?mediaId=157&monthId={month_id}&utilType=3"


# 发送请求
response = requests.get(url)

# 使用beautifusoup解析
soup = bs(response.text, "html.parser")

# 获取表单信息
table = soup.find("table", attrs={"class": "qtab01"})


# Extract table data
data = []
for tr in table.find_all("tr"):
    # 判断tr的class属性是否为thHeight(表头)
    if tr.get("class") == ["thHeight"]:
        continue
    else:
        row = []
        for td in tr.find_all("td"):
            # 判断td的class属性是否为redball01(正确号码)
            if td.find("span", attrs={"class": "redball01"}):
                td_text = "r" + td.text
            else:
                td_text = td.text
            row.append(td_text)
        data.append(row[:-3])


# 将data写入到excel中
df = pd.DataFrame(data)
df.to_excel("./Data/data.xlsx", index=False, header=False)
