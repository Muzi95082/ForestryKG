# coding: utf-8
# 将csv转化为词向量
from read_csv import readCSVbyColumn
from pyfasttext import FastText


def create_predict(HudongItem_csv):
    predict_List = readCSVbyColumn(HudongItem_csv, 'title')
    file_object = open('vector_forestry.txt', 'a')
    model = FastText('wiki.zh.bin')


