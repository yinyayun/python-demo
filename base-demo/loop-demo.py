#coding:utf-8

list =["yin","ya","yun"]
str="allen"
'''
遍历list
'''
print "遍历list"
for element in list:
    print element
'''
通过range，遍历下标
'''
print "通过range，遍历下标"
for i in  range(len(list)):
    print list[i]


print "通过enumerate"
for (index,element) in  enumerate(list):
    print "index：%d,element:%s"%(index,element)


'''
采用牛X的方式构建List
'''
xxx=[x*2 for x in range(10,20) if x%2 == 0]
print "采用牛X的方式构建List=%s"%xxx

