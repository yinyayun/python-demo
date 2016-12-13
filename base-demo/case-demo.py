#coding:utf-8
print "请输入任意数字"

number= int(raw_input())

if number>10:
    print "大于10"
    print "有缩进-大于10"
elif number>100:
    print "大于100"

else:
    print "小于10"