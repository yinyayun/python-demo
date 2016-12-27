#coding:utf-8
import  matplotlib.pyplot as plt
import numpy as np

'''
绘制sin函数
'''
def drawSin0():
    x=np.arange(-np.pi,np.pi,0.01)
    y=np.sin(x)
    plt.plot(x,y,'b')
    plt.show()
'''
显示多图
'''
def drawSinAndCos():
    x=np.arange(-np.pi,np.pi*2,0.01)
    y1=np.sin(x)
    y2=np.cos(x)
    plt.figure(figsize=(8, 6), dpi=80)
    plt.xlim(x.min() * 1.1, x.max() * 1.1)  # 设置X轴区间
    plt.grid(True)#显示网格
    plt.plot(x,y1,'b')
    plt.plot(x,y2,'g')
    plt.show()

'''
调整刻度显示,显示线条注释
'''
def drawSinAndCos1():
    x=np.arange(-np.pi,np.pi*2,0.01)
    y1=np.sin(x)
    y2=np.cos(x)
    #plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi])#只显示这些刻度
    plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],[r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])#设置刻度的显示名称
    plt.yticks([-1,0,1])  # 只显示这些刻度
    plt.plot(x,y1,color="green",linewidth=1.0,linestyle="-",label="sin")
    plt.plot(x,y2,color="blue",linewidth=1.0,linestyle="-",label="cos")
    plt.legend(loc='upper left')#结合plot(label='')显示注释
    plt.show()

'''
移动坐标
'''
def drawSinAndCos2():
    x=np.arange(-np.pi,np.pi*2,0.01)
    y1=np.sin(x)
    y2=np.cos(x)
    #######移动坐标
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data', 0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))
    #######
    plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],[r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])#设置刻度的显示名称
    plt.yticks([-1,0,1])  # 只显示这些刻度
    plt.plot(x,y1,color="green",linewidth=1.0,linestyle="-",label="sin")
    plt.plot(x,y2,color="blue",linewidth=1.0,linestyle="-",label="cos")
    plt.legend(loc='upper left')#结合plot(label='')显示注释
    plt.show()


'''
某点加粗,并给出标注
'''
def drawSinAndCos3():
    x=np.arange(-np.pi,np.pi*2,0.01)
    y1=np.sin(x)
    y2=np.cos(x)
    #######移动坐标
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data', 0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))
    #######
    t = np.pi / 2
    plt.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],[r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])#设置刻度的显示名称
    plt.yticks([-1,0,1])  # 只显示这些刻度
    plt.plot(x,y1,color="green",linewidth=1.0,linestyle="-",label="sin")
    ######
    plt.scatter(t, np.sin(t), 50, color='green')#加粗sin上的某点
    plt.annotate("high point".decode("utf-8"),xy=(t, np.sin(t)))
    ######
    plt.plot(x,y2,color="blue",linewidth=1.0,linestyle="-",label="cos")
    plt.legend(loc='upper left')#结合plot(label='')显示注释
    plt.show()

'''
散点图
'''
def drawScatter():
    n = 1024
    X = np.random.normal(0, 1, n)
    Y = np.random.normal(0, 1, n)
    plt.scatter(X, Y)
    plt.show()

'''
绘制方阵
'''
def drawBar():
    n = 12
    X = np.arange(n)
    Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
    Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
    plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
    plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')
    for x, y in zip(X, Y1):
        plt.text(x, y + 0.05, '%.2f' % y, ha='center', va='bottom')
        #plt.text(x, -y - 0.1, '%.2f' % y, ha='center', va='bottom')
    plt.ylim(-1.25, +1.25)
    plt.show()

def f(x, y): return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)
'''
绘制等高线
'''
def drawContour():
    n = 256
    x = np.linspace(-3, 3, n)
    y = np.linspace(-3, 3, n)
    X, Y = np.meshgrid(x, y)
    plt.contourf(X, Y, f(X, Y), 8, alpha=.75, cmap='jet')
    plt.contour(X, Y, f(X, Y), 8, colors='black', linewidth=.5)
    plt.show()

'''
绘制Imshow
'''
def drawImshow():
    n = 10
    x = np.linspace(-3, 3, 4 * n)
    y = np.linspace(-3, 3, 3 * n)
    X, Y = np.meshgrid(x, y)
    plt.imshow(f(X, Y))
    plt.show()

'''
绘制饼图
'''
def drawPie():
    n = 20
    Z = np.random.uniform(0, 1, n)
    plt.pie(Z)
    plt.show()

if __name__ == '__main__':
    drawPie()