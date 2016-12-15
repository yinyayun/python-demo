#coding:utf-8
from sklearn import svm
import  numpy as np
import pickle
from traindata import TrainData


'''
print len(digits.data)
print digits.data #特征数据，即训练数据
print len(digits.target)
print digits.target #标签数据
'''

#构建svc分类器
#print clf.predict(np.array(digits.data[-1]).reshape(1,-1))

def doSvc(feature,tags):
    print "构建svc支持向量分类..."
    clf = svm.SVC(gamma=0.001, C=100.0)
    print "进行训练..."
    clf.fit(feature, tags)
    #保存模型
    print "保存模型"
    return pickle.dumps(clf)

if __name__ == '__main__':
    # digits = datasets.load_digits() #加载数字图像数据集
    model= doSvc(TrainData.digits.data,TrainData.digits.target)
    print "加载模型"
    svcModel = pickle.loads(model)
    print "预测第一个数据的标签:"
    print svcModel.predict(np.array(TrainData.digits.data[0]).reshape(1,-1))
