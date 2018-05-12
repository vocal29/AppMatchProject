with open("D:\\work\\apk\\matchDemoAllDot7.txt", "r", encoding='utf8') as f:
    lines = f.readlines()
    # print(lines)
# 修改不合理数据
with open("D:\\work\\apk\\matchDemoAllModifyDot7.txt", "w", encoding='utf8') as f_w:
    for line in lines:
        app_name = line.split(",")[0].strip()
        # WhatsApp 匹配不准确
        # if "WhatsApp" == app_name:
        #     modify_1 = line.replace("Photography", "Social")
        #     modify_2 = modify_1.replace(
        #         "Camera For Whatsapp,8.5 MB,3.9,0.7295766472816467",
        #         "WhatsApp Messenger,12.2 MB,3.9,0.888")
        #     f_w.write(modify_2)
        #     # print(modify_2)
        #     continue
        # 删掉格式不符合标准的数据
        if "," not in line:
            print(1)
            continue
        elif line.count(",") < 14:
            continue
        f_w.write(line)

# 清洗出未匹配到数据
with open("D:\\work\\apk\\matchDemoAllModifyDot7.txt", "r", encoding='utf8') as f:
    lines_1 = f.readlines()
    # print(lines_1)
with open("D:\\work\\apk\\xenderDemo.txt", "r", encoding='utf8') as ff:
    lines_2 = ff.readlines()
    # print(lines_2)
with open("D:\\work\\apk\\matchDemoAllRestDot7.txt", "w", encoding='utf8') as f_w:
    for line_2 in lines_2:
        xender_name = line_2.split(",")[0].strip()
        match_number = 0
        for line_1 in lines_1:
            match_name = line_1.split(",")[0].strip()
            if xender_name == match_name:
                match_number += 1
        if match_number == 0:
            f_w.write(line_2)








