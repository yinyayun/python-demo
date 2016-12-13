#coding:utf-8

list1=["yin","ya","yun"]
list2=["allen"]
'''
长度
'''
print "list1长度：%d"%len(list1)

'''
合并list
'''
list1.extend(list2)

print "合并后list1：%s,list2:%s"%(str(list1),str(list2))

'''
list合并字符串
'''
extStr="yyy"
list1.extend(extStr)
print "合并后list1：%s,list2:%s"%(str(list1),str(list2))

'''
list append
'''

list2.append("same")
print "合并后list1：%s,list2:%s"%(str(list1),str(list2))

'''
读取list值
'''
print "list2的第二个元素为:%s"%list2[1]

'''
统计某个元素的个数
'''
print "list1中y元素的个数为:%d"%list1.count("y")

'''
检索元素的位置
'''
print "list1中allen元素所在位置:%d"%list1.index("allen")

'''
读取list某个下标以后的数据
'''
print "list1下标2以后的数据：%s"%list1[2:]


#尝试使用map,filter构建
print "尝试使用map,filter"
print map(lambda x:x,range(6))
print filter(lambda x:x>3,range(6))