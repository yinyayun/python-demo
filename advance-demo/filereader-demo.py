#coding:utf-8
#读文件
import os
def count(path,char='h'):
    count=0
    file=open(path,'r')
    for line in file.readlines():
        count += len(filter(lambda ch:ch==char,line.strip()))
    file.close()
    return count

print "统计count.txt中y字符的个数为：%d"%count("../data/count.txt")
print "统计count.txt中o字符的个数为：%d"%count("../data/count.txt",'o')