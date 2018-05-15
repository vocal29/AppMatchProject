import requests
from bs4 import BeautifulSoup
from urllib import parse
import pymongo
import re
import logging
import time


# 连接MongoDB
client = pymongo.MongoClient('localhost', 27017)
# 新建数据库
mydb = client['apkpure']
info = mydb['apksupplement']
# 开始计时
time_begin = time.localtime(time.time())
print(time_begin)
with open("D:\\work\\apk\\restSearchTimeCount.txt", "a") as f:
    f.write("time_begin:" + "{}".format(time_begin) + '\n')
logging.basicConfig(
    format='%(asctime)s : %(levelname)s : %(message)s',
    level=logging.INFO)
# APKPure首页
with open("D:\\work\\apk\\restDemoClean.txt", "r", encoding="utf8") as f:
    lines = f.readlines()
line_number = 0
for line in lines:
    line_number += 1
    if line_number >= 1:
        # noinspection PyBroadException
        try:
            search = line[0:-1]
            print(search)
            search_url = parse.quote(search, 'utf-8')
            url00 = 'https://apkpure.com/search?q={}'.format(search_url)
            print(url00)
            # app分类数据
            rank_data = requests.get(url00)
            # print(rank_data.text)
            soup00 = BeautifulSoup(rank_data.text, 'html.parser')
            # print(soup00)
            first_app = soup00.find('p', {'class': 'search-title'})
            app_name = first_app.find('a')
            url_name = app_name['href']
            # print(app_name.text)
            # print(url_name)
            apk_name = app_name.text
            apk_url = 'https://apkpure.com' + url_name
            print(apk_url)
            apk_data = requests.get(apk_url)
            soup01 = BeautifulSoup(apk_data.text, 'html.parser')
            apk_class_region = soup01.find(
                'div', {'class': 'title bread-crumbs'})
            # print(app_class_region.text)
            result = re.findall(".*»(.*)».*", apk_class_region.text)
            app_class = ""
            for x in result:
                app_class += x
            apk_class = app_class.strip()
            size_code = soup01.find('span', {'class': 'fsize'})
            if size_code is None:
                apk_size = "N/A"
            else:
                apk_size = size_code.find('span').text.strip()
            score_code = soup01.find('span', {'class': 'average'})
            if score_code is None:
                apk_score = "0.0"
            else:
                apk_score = soup01.find(
                    'span', {'class': 'average'}).text.strip()
            # version_code = soup01.find('div', {'class': 'details-sdk'})
            # if version_code is None:
            #     apk_version = "N/A"
            # else:
            #     apk_version = soup01.find('div', {'class': 'details-sdk'}).text.strip()
            # developer_code = soup01.find('div', {'class': 'details-author'})
            # if developer_code is None:
            #     apk_developer = "N/A"
            # else:
            #     apk_developer = soup01.find('div', {'class': 'details-author'}).text.strip()

            info.insert_one(
                {
                    'name': '{}'.format(apk_name),
                    'class': '{}'.format(apk_class),
                    'score': '{}'.format(apk_score),
                    # 'version': '{}'.format(apk_version),
                    'size': '{}'.format(apk_size),
                    # 'developer': '{}'.format(apk_developer)
                })
            print(
                apk_name,
                apk_size,
                apk_class,
                apk_score,
                # apk_version,
                # apk_developer
            )
            # 存储查询后的xender_name
            with open("D:\\work\\apk\\restDemoCrawled.txt", "a", encoding='utf8') as ff:
                ff.write(search + '---------------' + apk_name + '\n')
        except BaseException:
            continue
# 结束计时
time_end = time.localtime(time.time())
print(time_end)
with open("D:\\work\\apk\\restSearchTimeCount.txt", "a") as f:
    f.write("time_end" + "{}".format(time_end) + '\n')
print(time.clock())
