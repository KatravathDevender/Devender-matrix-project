import numpy as np
import matplotlib.pyplot as plt

b=np.sqrt(8)
a=(np.sqrt(2))*b
c=np.sqrt((a*a)-(b*b))

A=np.array([a,0])
A1=np.array([-a,0])
F=np.array([c,0])
F1=np.array([-c,0])
B=np.array([0,b])
B1=np.array([0,-b])
O=np.array([0,0])

len=1000
size=np.linspace(0,1,len)
E=np.linspace(-1,1,len)
x_AB1=np.zeros((2,len))
x_AB2=np.zeros((2,len))
x_AB3=np.zeros((2,len))
x_AB4=np.zeros((2,len))
x_AB5=np.zeros((2,len))
x_AB6=np.zeros((2,len))

for i in range(len):
   cos=E[i]
   sin=np.sqrt(1-(E[i]*E[i]))
   x1=a*cos
   y1=b*sin
   x2=x1
   y2=-y1
   z1=np.array([x1,y1])
   x_AB1[:,i]=z1.T
   z2=np.array([x2,y2])
   x_AB2[:,i]=z2.T
   
   line1=A1+size[i]*(A-A1)
   x_AB3[:,i]=line1.T
    
   line2=F1+size[i]*(B-F1)
   x_AB4[:,i]=line2.T
    
   line3=F+size[i]*(B-F)
   x_AB5[:,i]=line3.T
   
   line4=B1+size[i]*(B-B1)
   x_AB6[:,i]=line4.T
   
   
   
plt.plot(x_AB1[0,:],x_AB1[1,:],'b')
plt.plot(x_AB2[0,:],x_AB2[1,:],'b')
plt.plot(x_AB3[0,:],x_AB3[1,:],'r')
plt.plot(x_AB4[0,:],x_AB4[1,:],'y')
plt.plot(x_AB5[0,:],x_AB5[1,:],'y')
plt.plot(x_AB6[0,:],x_AB6[1,:],'r')


plt.plot(A[0],A[1],'o')
plt.plot(A1[0],A1[1],'o')
plt.plot(F[0],F[1],'o')
plt.plot(F1[0],F1[1],'o')
plt.plot(O[0],O[1],'o')
plt.plot(B[0],B[1],'o')
plt.plot(B1[0],B1[1],'o')

plt.text(A[0]*(1+0.03),A[1]+(0.05),'A (a,0)')
plt.text(A1[0]*(1+0.1),A1[1]+(0.05),'A1 (-a,0)')
plt.text(F[0]*(1+0.03),F[1]+(0.05),'F (c,0)')
plt.text(F1[0]*(1+0.1),F1[1]+(0.05),'F1 (-c,0)')
plt.text(O[0]*(1-0.03),O[1]+(0.05),'O (0,0)')
plt.text(B[0]+(0.05),B[1]*(1+0.03),'B (0,b)')
plt.text(B1[0]+(0.05),B1[1]*(1+0.03),'B (0,b)')


plt.legend(loc='best')
plt.grid()
plt.show()
