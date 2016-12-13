#coding:utf-8

'''
()是元祖的符号
{}为dict的符号
[]为list符号
元祖与list的区别在于，list的元素可以修改，而元祖不可以。相同的地方都是集合，且元素可以是任意类型
'''
array=123,456
print array

array=123,345,(123,345),[123,123]
print array

'''
读取元祖某个下标以后的数据
'''
print array[2:]
print array[2:3]

#是否包含
if 123 in array:
    print "元祖：%s存在元素:%s"%(array,123)
if 234 not in array:
    print "元祖：%s不存在元素:%s" % (array, 234)

#
array2=array*2
print "元祖x2动作:%s"%str(array2)


#切片动作
print "切片动作"
print "翻转:%s"%str(array[::-1])
print "跳跃取值:%s"%str(array[::2])