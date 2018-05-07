import json
import re
for line in open("D:\\work\\apk\\apkPureEn.json", "r", encoding="utf8"):
    # noinspection PyBroadException
    try:
        apk_apps = json.loads(line)
        app_apkpure_name = apk_apps["name"].strip()
        app_apkpure_class = apk_apps["class"].strip()
        app_apkpure_size = apk_apps["size"].strip()
        app_apkpure_socre = apk_apps["score"].strip()
        k = '[,，]+'
        app_apkpure_name_2 = re.sub(k, ' ', app_apkpure_name)
        # print(app_apkpure_name_2)
        app_apkpure_name_3 = re.search(r".+(?=[\-|—]+)", app_apkpure_name_2)
        if app_apkpure_name_3 is not None:
            name_clean = app_apkpure_name_3.group(0)
        else:
            name_clean = app_apkpure_name_2
        name_final = re.sub(r"\s{2,}", " ", name_clean)
        print(name_final)
        with open("D:\\work\\apk\\apkPureUn.txt", "a", encoding="utf8") as ff:
            ff.write(
                "{0},{1},{2},{3}".format(
                    name_final.strip(),
                    app_apkpure_class,
                    app_apkpure_size,
                    app_apkpure_socre + '\n'))
    except BaseException:
        continue
