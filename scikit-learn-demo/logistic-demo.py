#coding:utf-8
import  numpy as np
from sklearn import metrics
from sklearn.linear_model import LogisticRegression

from  traindata import TrainData
def doLogistic(feature,tag):
    print "构建逻辑回归模型..."
    model = LogisticRegression()
    print "训练逻辑回归模型..."
    model.fit(feature, tag)
    return model


if __name__ == '__main__':
  model =  doLogistic(TrainData.digFeature,TrainData.digTag)
  print "模型预测..."
  predicted = model.predict(np.array(TrainData.digFeature[0]).reshape(1,-1))
  print "predicted:%s"%predicted
  print "概率..."
  print metrics.classification_report(np.array(TrainData.digTag[0]).reshape(-1), predicted)
  print metrics.confusion_matrix(np.array(TrainData.digTag[0]).reshape(-1), predicted)