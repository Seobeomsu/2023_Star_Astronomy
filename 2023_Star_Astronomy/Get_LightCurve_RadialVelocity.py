import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# 파일 경로 및 이름 지정
filename = "YYSgr.txt"
# 파일열기
f = open(filename, 'r')
YYsgr = []
for line in f.readlines():
    col = line.strip().split(' ')
    YYsgr.append(col)
f.close()

test = []
for i in range(len(YYsgr)):
    if i != 0:
      test.append(YYsgr[i])
YYsgr = np.array(test)

t_P = [] ; v1r = [] ; v2r = [] ; Mbol = []
for _ in range(0, 1002):
    t_P.append(float(YYsgr[_][0]))
    v1r.append(float(YYsgr[_][1]))
    v2r.append(float(YYsgr[_][2]))
    Mbol.append(float(YYsgr[_][3]))
# 광도곡선 그리기
plt.plot(t_P,Mbol,label="Mbol")
plt.axis([0, 1, -1.25, -2.8])
plt.xlabel('t/P')
plt.ylabel('Mbol')
plt.title('Light Curve')
plt.legend()
plt.show()
# 시선속도 그리기
plt.plot(t_P,v1r,label='v1r')
plt.plot(t_P,v2r,label='v2r')
plt.xlabel('t/P')
plt.ylabel('V(km/s)')
plt.title('Radial Velocity')
plt.legend()
plt.show()