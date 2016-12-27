#coding:utf-8
import nltk as nk
from nltk.book import text1 as t1
from nltk.book import text4 as t4
print '================================='
'''
下载测试数据
'''
# nltk.download()

print '===============查找关键词=================='
t1.concordance("america")

print '===============查找相似上下文==============='
t1.similar("america")

print '=============共同的语法结构================='
t1.common_contexts(['in','of'])

print '=================词汇分布图================='
t4.dispersion_plot(['citizens','democaracy','freedom','america'])

print '=================统计最常出现的词================'
freList=nk.FreqDist(t1)
freList.plot(50,cumulative=False)

print '=================统计长度超过15的词==============='
v=set(t1)
long_words=filter(lambda x:len(x)>15,v)[:10]
print long_words

print '=================常用双连词搭配==============='
tuple= nk.bigrams(['all','in','of','take','like'])
for x in tuple:
    print x

print '=================基于语料的双连词搭配==============='
t1.collocations()