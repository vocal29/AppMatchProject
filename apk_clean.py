import json
import re

# # 清洗apkPure中name里面的逗号和-连接的app介绍
# for line in open("D:\\work\\app\\apkPureEn.json", "r", encoding="utf-8"):
#     # noinspection PyBroadException
#     try:
#         apk_apps = json.loads(line)
#         app_apkpure_name = apk_apps["name"].strip()
#         app_apkpure_class = apk_apps["class"].strip()
#         app_apkpure_size = apk_apps["size"].strip()
#         app_apkpure_socre = apk_apps["score"].strip()
#         k = '[,，]+'
#         app_apkpure_name_2 = re.sub(k, ' ', app_apkpure_name)
#         # print(app_apkpure_name_2)
#         app_apkpure_name_3 = re.search(r".+(?=[\-|—]+)", app_apkpure_name_2)
#         if app_apkpure_name_3 is not None:
#             name_clean = app_apkpure_name_3.group(0)
#         else:
#             name_clean = app_apkpure_name_2
#         name_final = re.sub(r"\s{2,}", " ", name_clean)
#         print(name_final)
#         with open("D:\\work\\app\\apkPureEn2.txt", "a") as ff:
#             ff.write(
#                 "{0},{1},{2},{3}".format(
#                     name_final.strip(),
#                     app_apkpure_class,
#                     app_apkpure_size,
#                     app_apkpure_socre + '\n'))
#     except BaseException:
#         continue


# 洗出name用以做字典
f = open('D:\\work\\apk\\apkPureEn.txt', 'r')
line = f.readline()
# num_match = 0
for i in range(17750):
    # apk_name清洗
    app_apkpure_name_clean = line.split(',')[0].lower().strip()
    r = '[’!"#$%&\'()*+,-./:;<=>?@^_`{|}~（）—]+'
    app_apkpure_name_clean_2 = re.sub(r, ' ', app_apkpure_name_clean)
    name_final = re.sub(r"\s{2,}", " ", app_apkpure_name_clean_2)
    print(name_final)
    # 存储清洗后的xender_name
    with open("D:\\work\\apk\\apkPureEnClean.txt", "a") as ff:
        ff.write(name_final + '\n')
    line = f.readline()
f.close()
