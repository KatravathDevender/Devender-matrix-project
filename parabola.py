import numpy as np
import matplotlib.pyplot as plt

len1=1000
x_AB1=np.zeros((2,len1))
x_AB2=np.zeros((2,len1))
d=np.linspace(0,5,len1)

len2=2
e=np.array([0.5,1])

len3=20
f=np.linspace(-1,5,len3)
x_AB3=np.zeros((2,len3))
x_AB4=np.zeros((2,len3))
x_AB5=np.zeros((2,len3))
for i in range (len1):
    m=d[i]*d[i]
    n1=2*d[i]
    n2=-n1
    para1=np.array([m,n1])
    x_AB1[:,i]=para1.T
    para2=np.array([m,n2])
    x_AB2[:,i]=para2.T
       
plt.plot(x_AB1[0,:],x_AB1[1,:],'r')
plt.plot(x_AB2[0,:],x_AB2[1,:],'r')    
for j in range(len2):
	   a=e[j]
	   x1=a*a
	   y1=2*a
	   b=(-1)*(1/a)
	   x2=b*b
	   y2=2*b
	   plt.plot(x1,y1,'o')
	   plt.text(x1*(1+0.2),y1*(1-0.2),'P')
	   plt.plot(x2,y2,'o')
	   plt.text(x2*(1),y2*(1),'Q')
	   for k in range (len3):
		   x3=f[k]
		   y3=a+(x3/a)
		   y4=b+(x3/b)
		   z3=np.array([x3,y3])
		   x_AB3[:,k]=z3.T
		   z4=np.array([x3,y4])
		   x_AB4[:,k]=z4.T
		   z5=np.array([-1,3*(x3-2)])
		   x_AB5[:,k]=z5.T
	   plt.plot(x_AB3[0,:],x_AB3[1,:],'b')
	   plt.plot(x_AB4[0,:],x_AB4[1,:],'c')
	   plt.plot(x_AB5[0,:],x_AB5[1,:],'k')
	   plt.text(-0.95,-7.5,'x=-1')
	   plt.text(8,5.3,'y^2=4x')
       

plt.legend(loc='best')
plt.grid()
plt.show()
