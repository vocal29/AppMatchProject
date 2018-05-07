from gensim import corpora, models, similarities
import logging
import numpy as np
import time


def load(app_to_classify):
    infile = open("D:\\work\\apk\\apkPureEnClean.txt", 'r')
    words = []
    # 加载数据
    for line in infile:
        # print(line[0:-1])
        words.append(line[0:-1])
    infile.close()
    # 切词
    global app_names
    app_names = [[word for word in words.split(" ")] for words in words]
    # 加载字典
    dictionary = corpora.Dictionary.load_from_text(
        'D:\\work\\apk\\apkNameDic.dict')
    # 加载模型
    tfidf_model = models.TfidfModel.load(
        "D:\\work\\apk\\apkTfidfModel.tfidf")  # type: np.ndarray
    word_model = app_names
    corpus_model = [dictionary.doc2bow(test) for test in word_model]
    test_word = app_to_classify
    test_bow = dictionary.doc2bow([word for word in test_word.split(' ')])
    print(test_bow)
    print(tfidf_model[test_bow])
    if len(test_bow):
        # 如果test_bow为空直接跳过检索
        # 在Tfidf基础之上，进行相似性检索
        index = similarities.SparseMatrixSimilarity(
            tfidf_model[corpus_model], num_features=13077)
        sims = index[tfidf_model[test_bow]]
        # print(list(enumerate(sims)))
        # 相似度排名
        rank = sorted(enumerate(sims), key=lambda item: -item[1])
        pair = rank[0]
        if pair[1] >= 0.7:
            # 返回满足相似度的样本材料,(index_of_document, similarity) tuples
            print("与{0}相匹配的app名称列表".format(app_names_init))
            print(pair)
            data_init = open("D:\\work\\apk\\apkPureEn.txt", 'r')
            app_apkpure_list = data_init.readlines()[pair[0]]
            app_apkpure_name = app_apkpure_list.split(',')[0]
            app_apkpure_class = app_apkpure_list.split(',')[1]
            app_apkpure_size = app_apkpure_list.split(',')[2]
            app_apkpure_score = app_apkpure_list.split(',')[3][0:-1]
            app_apkpure_similarity = pair[1]
            data_init.close()
            data = open("D:\\work\\apk\\xenderDemo.txt", 'r')
            app_data_list = data.readlines()[num]
            app_name_init = app_data_list.split(",")[0]
            app_kind_init = app_data_list.split(",")[1]
            app_md5_init = app_data_list.split(",")[2]
            app_sender_init = app_data_list.split(",")[3]
            app_receiver_init = app_data_list.split(",")[4]
            app_time_init = app_data_list.split(",")[5]
            app_ip_init = app_data_list.split(",")[6]
            app_region_init = app_data_list.split(",")[7]
            app_na_init = app_data_list.split(",")[8]
            app_size_init = app_data_list.split(",")[9][0:-1]
            data.close()
            global f
            with open("D:\\work\\apk\\matchDemoDot7.txt", "a") as f:
                f.write(
                    '{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13},{14}' .format(
                        app_name_init,
                        app_apkpure_class,
                        app_kind_init,
                        app_md5_init,
                        app_sender_init,
                        app_receiver_init,
                        app_time_init,
                        app_ip_init,
                        app_region_init,
                        app_na_init,
                        app_size_init,
                        app_apkpure_name,
                        app_apkpure_size,
                        app_apkpure_score,
                        app_apkpure_similarity) + '\n')


def main():
    infile_init = open("D:\\work\\apk\\xenderClean.txt", 'r')
    words_init = []
    # 加载数据
    line_num = 0
    for line in infile_init:
        line_num += 1
        if 68001 <= line_num <= 88393:
            # print(line[0:-1])
            words_init_0 = line[0:-1]
            words_init.append(words_init_0)
        # print(line_num)
    infile_init.close()
    # 切词
    global app_names_init
    global num
    num = 68000
    for app_names_init in words_init:
        # app_names_init = app_name_init.split(" ")
        load(app_names_init.lower())
        num += 1


if __name__ == '__main__':
    time_begin = time.localtime(time.time())
    print(time_begin)
    with open("D:\\work\\apk\\timeCountDot7.txt", "a") as f:
        f.write("time_begin_5:" + "{}".format(time_begin) + '\n')
    logging.basicConfig(
        format='%(asctime)s : %(levelname)s : %(message)s',
        level=logging.INFO)
    main()
    time_end = time.localtime(time.time())
    print(time_end)
    with open("D:\\work\\apk\\timeCountDot7.txt", "a") as f:
        f.write("time_end_5" + "{}".format(time_end) + '\n')
    print(time.clock())
