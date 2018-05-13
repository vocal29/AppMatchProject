import requests
from bs4 import BeautifulSoup
from urllib import parse
import pymongo
import re


# 连接MongoDB
client = pymongo.MongoClient('localhost', 27017)
# 新建数据库
mydb = client['apkpure']
info = mydb['apksupplement']
# APKPure首页
with open("D:\\work\\apk\\restDemo.txt", "r", encoding="utf8") as f:
    lines = f.readlines()
for line in lines:
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
        apk_class_region = soup01.find('div', {'class': 'title bread-crumbs'})
        # print(app_class_region.text)
        result = re.findall(".*»(.*)».*", apk_class_region.text)
        app_class = ""
        for x in result:
            app_class += x
        apk_class = app_class.strip()
        apk_size_list = soup01.find('span', {'class': 'fsize'})
        apk_size = apk_size_list.find('span').text
        apk_score = '0.0'
        info.insert_one(
            {
                'name': '{}'.format(apk_name),
                'class': '{}'.format(apk_class),
                'score': '{}'.format(apk_score),
                # 'version': '{}'.format(app_version),
                'size': '{}'.format(apk_size),
                # 'developer': '{}'.format(app_developer),
            })
        print(
            apk_name,
            apk_size,
            apk_class,
            apk_score,
            # app_version,
            # app_developer
        )
    except BaseException:
        continue
