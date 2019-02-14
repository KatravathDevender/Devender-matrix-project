import numpy as np
import matplotlib.pyplot as plt
P=np.array([1,0])
C=np.array([-1,-2])
r=2*(np.sqrt(2))
len=5000
x_PC=np.zeros((2,len))
D=np.linspace(0,2,len)
circle1=np.zeros((2,len))
circle2=np.zeros((2,len))
B=np.linspace(-1,1,len)

for i in range(len):
	line1=P+D[i]*(C-P)
	x_PC[:,i]=line1.T
	x=B[i]
	y1=np.sqrt(1-(B[i]*B[i]))
	y2=-y1
	z1=np.array([x,y1])
	z2=np.array([x,y2])
	A1=C+r*z1
	A2=C+r*z2
	circle1[:,i]=A1.T
	circle2[:,i]=A2.T
	
Y=P+D[len-1]*(C-P)
print Y
plt.plot(x_PC[0,:],x_PC[1,:],label='$diameter$')
plt.plot(circle1[0,:],circle1[1,:],'r')
plt.plot(circle2[0,:],circle2[1,:],'r')

plt.plot(Y[0],Y[1],'o')
plt.text(Y[0]*(1+0.06),Y[1]*(1+0.06),'Y')
plt.plot(P[0],P[1],'o')
plt.text(P[0]*(1+0.1),P[1]*(1-0.1),'P (1,0)')
plt.plot(C[0],C[1],'o')
plt.text(C[0]*(1-0.1),C[1]*(1),'C (-1,-2)')

plt.legend(loc='best')
plt.grid()
plt.show()
