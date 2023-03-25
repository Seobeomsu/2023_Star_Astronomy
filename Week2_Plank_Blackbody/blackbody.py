import matplotlib.pyplot as plt
import numpy as np
import math as math

def E(A, T):
	top = 2.0*h*c**2
	exp = h*c/(A*1e-10*k*T)
	bottom = (A*1e-10)**5*(np.exp(exp)-1.0) # 800A 밑의 단위에서는 값이너무작아 오류발생
	return top/bottom*1e-13

def Whin(T):
	for _ in range(len(T)):
		print(T[_],"K - Max A=",0.2897/T[_]*10**8)
	return 0

def BV(T):
	A1=3650 ; A2= 4400 ; A3= 5500
	for _ in range(len(T)):
		B=E(A2,T[_])
		V=E(A3,T[_])
		BV=-2.5*(math.log10(B/V))
		print("T=",T[_],"B=",B,"V=",V,"B-V=",BV)
	return 0
	
c = 3*1e8
h = 6.626*1e-34
k = 1.38*1e-23
T = [8000.0,10000.0,12000.0]
A =[] # A의값 10단위로 1200개 정의 0은 계산시에러가떠 제외
for _ in range(1,1201):
	A.append(_*10)

data1 = []; data2= []; data3= []
for j in range(len(A)):
	data1.append(E(A[j],T[0]))
	data2.append(E(A[j],T[1]))
	data3.append(E(A[j],T[2]))

Whin(T)#Whin의 변위법칙 사용하여 최대치 파장 A옹스트롬 단위로 출력
BV(T)
plt.plot(A,data1,label="8000K")
plt.plot(A,data2,label="10000K")
plt.plot(A,data3,label="12000K")
plt.xlabel('A(10^-10m)')
plt.ylabel('Luminusity 10^+13')
plt.title('blackbody emission')
plt.legend()
plt.show()