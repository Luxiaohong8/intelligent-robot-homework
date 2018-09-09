import numpy as np
import matplotlib.pyplot as plt
from sympy import *

#四个gps的点
G1=[100,100,100,0.03]
G2=[0,0,0,0.06]
G3=[0,100,100,0.055]
G4=[100,0,0,0.06]

    
d=[109,13,14,9]

#新建的变量
x=symbols('x')
y=symbols('y')
z=symbols('z')
v=symbols('v')

c=3*(10**3)

#解方程
solution=solve([
    ((G1[0]-x)**2+(G1[1]-y)**2+(G1[2]-z)**2)-(c*(G1[3]-v)-d[0])**2,
    ((G2[0]-x)**2+(G2[1]-y)**2+(G2[2]-z)**2)-(c*(G2[3]-v)-d[1])**2,
    ((G3[0]-x)**2+(G3[1]-y)**2+(G3[2]-z)**2)-(c*(G3[3]-v)-d[2])**2,
    ((G4[0]-x)**2+(G4[1]-y)**2+(G4[2]-z)**2)-(c*(G4[3]-v)-d[3])**2],
    [x,y,z,v]
)

target=list(solution[0])

#画图
import mpl_toolkits.mplot3d  
ax=plt.subplot(111,projection='3d')  

for e in range(0,len(target)):
    target[e]=float(target[e])
        
x,y,z=np.linspace(target[0],G1[0],10),np.linspace(target[1],G1[1],10),np.linspace(target[2],G1[2],10)
ax.plot(x,y,z,c='r')

    
x,y,z=np.linspace(target[0],G2[0],10),np.linspace(target[1],G2[1],10),np.linspace(target[2],G2[2],10)
ax.plot(x,y,z,c='r')
    
x,y,z=np.linspace(target[0],G3[0],10),np.linspace(target[1],G3[1],10),np.linspace(target[2],G3[2],10)
ax.plot(x,y,z,c='r')
    
x,y,z=np.linspace(target[0],G4[0],10),np.linspace(target[1],G4[1],10),np.linspace(target[2],G4[2],10)
ax.plot(x,y,z,c='r')

ax.scatter(target[0],target[1],target[2], c='g', marker='1',s=300)
ax.scatter(G1[0],G1[1],G1[2], c='r', marker='o',s=300)
ax.scatter(G2[0],G2[1],G2[2], c='r', marker='o',s=300)
ax.scatter(G3[0],G3[1],G3[2], c='r', marker='o',s=300)
ax.scatter(G4[0],G4[1],G4[2], c='r', marker='o',s=300)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.savefig('test2png.png', dpi=100)    
plt.show()