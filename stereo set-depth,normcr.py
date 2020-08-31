import cv2 as cv
import numpy as np 
from matplotlib import pyplot as plot
import math as ma
p_left=np.zeros((3,4))
p_left[0][0]=640.0
p_left[0][1]=0
p_left[0][2]=640.0
p_left[0][3]=2176.0
p_left[1][0]=0
p_left[1][1]=480.0
p_left[1][2]=480.0
p_left[1][3]=552.0
p_left[2][0]=0
p_left[2][1]=0
p_left[2][2]=1.0
p_left[2][3]=1.4

p_right=np.zeros((3,4))
p_right[0][0]=640.0
p_right[0][1]=0
p_right[0][2]=640.0
p_right[0][3]=2176.0
p_right[1][0]=0
p_right[1][1]=480.0
p_right[1][2]=480.0
p_right[1][3]=792.0
p_right[2][0]=0
p_right[2][1]=0
p_right[2][2]=1.0
p_right[2][3]=1.4


imgL = cv.imread('stereo_l.png',0)
imgR = cv.imread('stereo_r.png',0)
stereo = cv.StereoSGBM_create(numDisparities=100, blockSize=9)
disp_map = stereo.compute(imgL,imgR).astype(np.float32)/60
plot.show()

k1,R1,t1,R1x,R1y,R1z,E1=cv.decomposeProjectionMatrix(p_left)
k2,R2,t2,R2x,R2y,R2z,E2=cv.decomposeProjectionMatrix(p_right)









t2[0][0]=t2[0][0]/t2[3][0]
t2[1][0]=t2[1][0]/t2[3][0]
t2[2][0]=t2[2][0]/t2[3][0]
t2[3][0]=t2[3][0]/t2[3][0]
t1[0][0]=t1[0][0]/t1[3][0]
t1[1][0]=t1[1][0]/t1[3][0]
t1[2][0]=t1[2][0]/t1[3][0]
t1[3][0]=t1[3][0]/t1[3][0]
v=t2-t1
f=k1[1][1]

b=abs(v[1][0])
x,y=disp_map.shape

depth_map=np.zeros((x,y))
print(np.max(disp_map))


for k in range(x):
	for j in range(y):
		if disp_map[k][j]!=0:

			depth_map[k][j]=f*b/(disp_map[k][j])
		else:
			disp_map[k][j]=1
			depth_map[k][j]=f*b/(disp_map[k][j])



plot.imshow(depth_map,'gray')
plot.show()

temp=cv.imread('template.png',0)
var_temp=np.var(temp)
var_imgR=np.var(imgR)
#result = cv.matchTemplate(img, temp, cv.TM_CCOEFF)
'''plot.imshow(temp,'gray')
plot.show()'''
a,b=imgR.shape
#msk=img[75 :152,275:352]
mean_imgR=imgR.mean()

mean_temp=temp.mean()

temp=temp-mean_temp




'''plot.imshow(img,'gray')
plot.show()'''
'''(749, 621)
[Finished in 110.9s]plot.imshow(temp,'gray')
plot.show()'''
x,y=temp.shape
op=np.zeros((x,y))

op2=np.zeros((a,b))

for i in range(a-x):
	for j in range(b-y):
		op3=imgR[i:i+x,j:j+y]
		var_op3=np.var(op3)
		op=(np.multiply(temp/2,op3/2))/(x*ma.sqrt((var_temp)*(var_op3)))

		t=op.mean()
		
		op2[i+int((x+1)/2)][j+int((y+1)/2)]=t

(_, maxVal, _, maxLoc) = cv.minMaxLoc(op2)
m,n=maxLoc
#(_, maxVal2, _, maxLoc2) = cv.minMaxLoc(result)
print(np.max(op2))
print(maxLoc)
#print(maxLoc2)
#print(x,y)
plot.imshow(op2,'gray')
plot.show()

print(depth_map[m+int(x/2)][n+int(y/2)])