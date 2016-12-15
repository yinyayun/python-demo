#coding:utf-8
from sklearn import datasets #从sklearn包中加载数据集模块
import  numpy as np

class TrainData:
    iris = datasets.load_iris()  # 加载鸢尾花数据集
    digits = datasets.load_digits()  # 加载数字图像数据集
    digFeature=digits.data
    digTag=digits.target