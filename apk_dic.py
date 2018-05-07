from gensim import corpora, models, similarities
import logging


def save():
    infile = open("D:\\work\\apk\\apkPureEnClean.txt", 'r')
    words = []
    # 加载数据
    for line in infile:
        # print(line[0:-1])
        words.append(line[0:-1])
    infile.close()
    # 切词
    app_names = [[word for word in words.split(" ")] for words in words]
    # print(app_names)
    # 生成字典
    dictionary = corpora.Dictionary(app_names, prune_at=2000000)
    # 保存生成的字典
    # dictionary.save('D:\\work\\apk\\appNameDic.dict')
    dictionary.save_as_text(
        'D:\\work\\apk\\apkNameDic.dict',
        sort_by_word=True)


def load():
    # 加载字典
    # dictionary.load('D:\\work\\apk\\apkNameDic.dict')
    dictionary = corpora.Dictionary.load_from_text(
        'D:\\work\\apk\\apkNameDic.dict')
    # print(dictionary.token2id)
    # for key in dictionary.iterkeys():
    #     print(key, dictionary.get(key), dictionary.dfs[key])
    # print(dictionary)
    # print(corpus, missing)
    # 保存语料库，保存的格式有多种形式， Market Matrix，Joachim’s SVMlight、Blei’s LDA-C、GibbsLDA++
    # 将向量化后的词典保存,保存后生成两个文件，一个corpora.mm，分别(文章序号(从1开始),词向量编号，次出现的次数)，一个corpora.mm.index
    infile = open("D:\\work\\apk\\apkPureEnClean.txt", 'r')
    words = []
    data = []
    # 加载数据
    wordCounts = {}
    for line in infile:
        # print(line[0:-1])
        words.append(line[0:-1])
    infile.close()
    # 切词
    app_names = [[word for word in words.split(" ")] for words in words]
    corpus = [dictionary.doc2bow(text) for text in app_names]

    corpora.MmCorpus.serialize('D:\\work\\apk\\apkCorpora.mm', corpus)
    corpus = corpora.MmCorpus('D:\\work\\apk\\apkCorpora.mm')
    # 需要转换成list
    corpus_list = list(corpus)
    # print(corpus_list)
    tfidf_model = models.TfidfModel(corpus_list)
    # 将Tfidf模型存储
    tfidf_model.save("D:\\work\\apk\\apkTfidfModel.tfidf")
    corpus_tfidf = tfidf_model[corpus_list]
    testword = "uc browser"
    test_bow = dictionary.doc2bow([word for word in testword.split(' ')])
    # print(test_bow)
    # # 将corpus转换成tfidf模型
    # corpus_model = tfidf_model[test_bow]
    print(tfidf_model[test_bow])
    # 计算tf-idf相似度
    index = similarities.SparseMatrixSimilarity(
        tfidf_model[corpus_list], num_features=13826)
    sims = index[tfidf_model[test_bow]]
    # 相似度排名
    rank = sorted(enumerate(sims), key=lambda item: -item[1])
    pair = rank[0]
    print(pair[0], pair[1])
    # c = list(enumerate(sims))
    # # print(c)
    # max_similarity = c[0][1]
    # max_bow = c[0][0]
    # for pair in c:
    #     current_similarity = pair[1]
    #     if current_similarity >= max_similarity:
    #         max_similarity = current_similarity
    #         max_bow = pair[0]
    # print("({0},{1})".format(max_bow, max_similarity))
    # # 整体转化为Lsi模型
    # lsi_model = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=5)
    # corpus_lsi = lsi_model[corpus_tfidf]
    # nodes = list(corpus_lsi)
    # print(nodes)
    # 打印各topic的含义
    # print(lsi_model.print_topics(5))
    # 计算Lsi相似度
    lsi = models.LsiModel(corpus_tfidf)
    corpus_lsi = lsi[corpus_tfidf]
    # similarity_lsi = similarities.Similarity('Similarity-LSI-index', corpus_lsi, num_features=13826, num_best=1)
    similarity_lsi = similarities.MatrixSimilarity(corpus_lsi)
    # 待匹配文档转化模型
    test_corpus_tfidf = tfidf_model[test_bow]
    test_corpus_lsi = lsi[test_corpus_tfidf]
    # # 更新Lsi的值
    # lsi.add_documents(test_corpus_lsi)
    # print(similarity_lsi[test_corpus_lsi])
    sims = similarity_lsi[test_corpus_lsi]
    # sorted(enumerate(sims), key=lambda item: -item[1])
    print(sorted(enumerate(sims), key=lambda item: -item[1])[0])


def main():
    save()
    load()


if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s : %(levelname)s : %(message)s',
        level=logging.INFO)
    main()
