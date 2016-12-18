#coding:utf-8

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties
from sklearn.cluster import KMeans
from sklearn import metrics

font = FontProperties(fname=r"c:\windows\fonts\msyh.ttc", size=10)
plt.figure(figsize=(8, 10))#窗口大小
plt.subplot(3, 2, 1)#绘制子图
x1 = np.array([1, 2, 3, 1, 5, 6, 5, 5, 6, 7, 8, 9, 7, 9])
x2 = np.array([1, 3, 2, 2, 8, 6, 7, 6, 7, 1, 2, 1, 1, 3])
X = np.array(list(zip(x1, x2))).reshape(len(x1), 2)
plt.xlim([0, 10])
plt.ylim([0, 10])
plt.title('样本'.decode("utf8"),fontproperties=font)
plt.scatter(x1, x2)
plt.show()

