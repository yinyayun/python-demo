#coding:utf-8

x=100

'''
整形和String连接
'''
print "python demo:" + `x` #反引号
print "python demo:"+str(x)  #``和repr一致
print "python demo:" +repr(x) #str和repr的区别在于，str是一种类型，而repr是一个函数

'''
字符串占位
'''
print "一个占位：%d"%1
print "两个占位:%d-%d"%(1,2)

'''
字符串检索
'''
str="0123456789"
print "字符串:%s,长度：%d,第三位为：%s"%(str,len(str),str[2])