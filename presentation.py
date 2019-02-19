import numpy as np
import matplotlib.pyplot as plt
C=np.array([1,-1])
r=5
len=5000
circle1=np.zeros((2,len))
circle2=np.zeros((2,len))
line1=np.zeros((2,len))
line2=np.zeros((2,len))
cos=np.linspace(-1,1,len)
size1=np.linspace(-4,6,len)
size2=np.linspace(-2,3,len)
con=(0.3333333333333)

for i in range(len):
    x=cos[i]
    y1=np.sqrt(1-(cos[i]*cos[i]))
    y2=-y1
    z1=np.array([x,y1])
    z2=np.array([x,y2])
    A1=C+r*z1
    A2=C+r*z2
    circle1[:,i]=A1.T
    circle2[:,i]=A2.T
    
    u1=size1[i]
    v1=(-1-2*(u1))*con
    u2=size2[i]
    v2=3*(u2)-4
    A3=np.array([u1,v1])
    A4=np.array([u2,v2])
    line1[:,i]=A3.T
    line2[:,i]=A4.T
  

plt.plot(circle1[0,:],circle1[1,:],'r')
plt.plot(circle2[0,:],circle2[1,:],'r')
plt.plot(line1[0,:],line1[1,:],'y')
plt.plot(line2[0,:],line2[1,:],'b')

plt.plot(C[0],C[1],'o')
plt.text(C[0]*(1-0.1),C[1]*(1),'C')
plt.text(-4.5,1.6,'2x+3y+1=0')
plt.text(-2.5,-10,'3x-y-4=0')


plt.legend(loc='best')
plt.grid()
plt.show()
