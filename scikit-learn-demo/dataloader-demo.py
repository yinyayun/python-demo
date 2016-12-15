#coding:utf-8
import numpy as np
import pandas as pd


dataset = np.loadtxt("../data/pima-indians-diabetes.data.txt", delimiter=",")
text= pd.read_table("../data/text.txt",sep='##')
print "=======pima-indians-diabetes.data======="
print dataset
print "=======pima-indians-diabetes.data======="

print "=======text.txt======="
print type(text)
print text
print "=======text.txt======="
