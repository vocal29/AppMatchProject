import re


# unicode编码
# with open("D:\\work\\apk\\xenderClean.txt", "r", encoding="utf8") as f:
#     lines = f.readlines()
# with open("D:\\work\\apk\\xenderCleanAll.txt", "w", encoding="utf8") as ff:
#     for line in lines:
#         # print(line)
#         # ff.write(line)
#         line_unicode = line.encode("latin-1").decode("unicode_escape")
#         k = '[,，®🙂🤑🏁™🌪👶♂♀・❤♥＜＞⚔😍♠♥♣♦🔥•©«»»¼¿؟ـ∞│▲▶►◉★☆☕🎬☠☣☼' \
#             '♪♬🇺🇸🌞🎧🎮⚽🎹🎉🏠🏡🏰	🐌🐙🐣🐻👑⚜💎👕👗👩🍳👰👶♂♀👽💃💍💖💤💧❄💩💰📱📺' \
#             '🔔🔠🔥🔫😂😄😈🐰😍🚗🚗💨🚓🚨🤰🥇🦋🦋🏖️🏎⛺🎸🏂🏆🎲🎈🎶🎼🎄🎵🌴✂🏍️🍀🌹✔🍳' \
#             '🍼✦🎃✪❄➨🁩🁡🂠🂫🆕🇹🇷]+'
#         e = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
#         app_apkpure_name_1 = re.sub(k, ' ', line_unicode)
#         app_apkpure_name_2 = re.sub(e, ' ', app_apkpure_name_1)
#         r = '[’\\!”“ ‘"#$%&\'()*+,-./:;<=>?@^_`{|}~（）—【】～：：－《》。、，­­「」‘\n［］[\]]+'
#         app_apkpure_name_clean_2 = re.sub(r, ' ', app_apkpure_name_2)
#         name_final = re.sub(r"\s{2,}", " ", app_apkpure_name_clean_2)
#         ff.write(name_final.strip() + '\n')


# 匹配剩余数据的转码
with open("D:\\work\\apk\\matchDemoAllRestDot7.txt", "r", encoding="utf8") as f:
    lines = f.readlines()
with open("D:\\work\\apk\\matchDemoAllRestUniDot7.txt", "w", encoding="utf8") as ff:
    for line in lines:
        # print(line)
        # ff.write(line)
        line_unicode = line.split(",")[0].encode("latin-1").decode("unicode_escape")
        # k = '[,，®🙂🤑🏁™🌪👶♂♀・❤♥＜＞⚔😍♠♥♣♦🔥•©«»»¼¿؟ـ∞│▲▶►◉★☆☕🎬☠☣☼' \
        #     '♪♬🇺🇸🌞🎧🎮⚽🎹🎉🏠🏡🏰	🐌🐙🐣🐻👑⚜💎👕👗👩🍳👰👶♂♀👽💃💍💖💤💧❄💩💰📱📺' \
        #     '🔔🔠🔥🔫😂😄😈🐰😍🚗🚗💨🚓🚨🤰🥇🦋🦋🏖️🏎⛺🎸🏂🏆🎲🎈🎶🎼🎄🎵🌴✂🏍️🍀🌹✔🍳' \
        #     '🍼✦🎃✪❄➨🁩🁡🂠🂫🆕🇹🇷]+'
        # e = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
        # app_apkpure_name_1 = re.sub(k, ' ', line_unicode)
        # app_apkpure_name_2 = re.sub(e, ' ', app_apkpure_name_1)
        # r = '[’\\!”“ ‘"#$%&\'()*+,-./:;<=>?@^_`{|}~（）—【】～：：－《》。、，­­「」‘\n［］[\]]+'
        # app_apkpure_name_clean_2 = re.sub(r, ' ', app_apkpure_name_2)
        # name_final = re.sub(r"\s{2,}", " ", app_apkpure_name_clean_2)
        ff.write(line_unicode.strip() + '\n')
