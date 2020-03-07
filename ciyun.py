#!/usr/bin/env python
# coding=utf-8
import os
import jieba
import numpy as np
from PIL import Image
from wordcloud import WordCloud, STOPWORDS
import collections  # 词频统计库
import re
import scrapy

CURDIR = os.path.abspath(os.path.dirname(__file__))
TEXT = os.path.join(CURDIR, 'ciyun.txt')
PICTURE = os.path.join(CURDIR, 'ciyun.png')
FONT = os.path.join(CURDIR, 'simsun.ttc')


def create_worlds_cloud():
    background = np.array(Image.open(PICTURE))
    stopwords = set(STOPWORDS)

    # 读取文件
    fn = open('ciyun.txt', encoding='utf-8')  # 打开文件
    string_data = fn.read()  # 读出整个文件
    fn.close()  # 关闭文件

    # 文本预处理
    pattern = re.compile(u'\t|\n|\.|-|:|;|\)|\(|\?|"')  # 定义正则表达式匹配模式
    string_data = re.sub(pattern, '', string_data)  # 将符合模式的字符去除

    # 文本分词
    seg_list_exact = jieba.cut(string_data, cut_all=True)  # 精确模式分词
    object_list = []
    remove_words = [', ', '']  # 自定义去除词库

    for word in seg_list_exact:  # 循环读出每个分词
        if word not in remove_words:  # 如果不在去除词库中
            object_list.append(word)  # 分词追加到列表

    # 词频统计
    word_counts = collections.Counter(object_list)  # 对分词做词频统计
    word_counts_top10 = word_counts.most_common(10)  # 获取前10最高频的词
    print(word_counts_top10)  # 输出检查

    wc = WordCloud(background_color="white",
                   mask=background,
                   stopwords=stopwords,
                   font_path=FONT,
                   max_words=200,  # 最多显示词数
                   # max_font_size=100  # 字体最大值
                   )
    wc.generate_from_frequencies(word_counts)
    wc.to_file('girl.png')


if __name__ == '__main__':
    create_worlds_cloud()

