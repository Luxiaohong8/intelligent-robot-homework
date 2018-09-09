
import matplotlib.pyplot as plt  
import numpy as np  
import math

def has_point(k,b):#最简单的实现返回那个点的坐标
    if k==0:
        return -1
    x2=(3-b)/k
    y1=k*1+b
    if x2<=3 and x2>=1:
        return x2,3.0
    elif y1<=3 and y1>=1:
        return 1.0,y1
    else:
        return -1

x=[1,1,3]
y=[1,3,3]#墙
plt.plot(x, y, 'g*')
plt.plot(x[:2], y[:2],'g')  
plt.plot(x[1:], y[1:],'g')  
thex=[]
they=[]

robot=[4, 0.5]#robot当前位置
plt.scatter(robot[0],robot[1],color='r',marker='1',s=300)

for i in range(0,180):
    deltat = i*math.pi/180#每次多转1度
    x1 = robot[0] + 10*math.cos(deltat)
    y1 = robot[1] + 10*math.sin(deltat)
    k=math.tan(deltat)
    b=y1-x1*k#计算当前发射信号的角度的函数
    if has_point(k,b)!=-1:
        [x2,y2]=has_point(k,b)
        thex.append(x2)
        they.append(y2)

plt.xlim(0,5)
plt.ylim(0,5)
    
plt.show()


plt.plot(thex,they, 'y*')
plt.scatter(robot[0],robot[1],color='r',marker='1',s=300)
for i in range(len(thex)):
    plt.plot([thex[i],robot[0]],[they[i],robot[1]],'b')  
plt.show()