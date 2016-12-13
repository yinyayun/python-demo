#coding:utf-8

map={1:"a",2:"b",3:"c"}
print map
print dict(zip(("java","c++","c"),(1000,2000,3000)))
print dict([["java",1000],["c++",2000]])
print  dict(java=1000,c = 2000)

'''
读取字典元素
'''
print "读取字典元素:"
print  map[2]

'''
增加字典元素
'''
print "增加字典元素:"
map[0]="abc"
print  map


'''
更新字典元素
'''
print "更新字典元素:"
map[1]="abc"
print  map

'''
通过元祖创建
'''
print "通过元祖创建:"
array =(["yinyayun","man"],["allen","man"])
people=dict(array)
print  people

'''
通过formkeys创建
'''
print "通过formkeys创建"
print {}.fromkeys(("key1","key2"),"value")

'''
遍历字典
'''
print "遍历字典"

for key in map:
    print  "%s:%s"%(key,map[key])
