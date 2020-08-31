import numpy as np 
import cv2 as cv
import random as rng
def nothing(x):
	pass
sett
max_val=255
max_val_h=360//2
low_h=0
low_s=0
low_v=0

high_h=max_val_h
high_s=max_val
high_v=max_val
window_name='og image'
threshold_window='threshold '
high_h_name='high h'
low_h_name='low h'
high_s_name='high s'
low_s_name='low s'
low_v_name='low v'
high_v_name='high v'
cam=cv.VideoCapture(0)
threshold_window='threshold_window'
cv.namedWindow(threshold_window)
#vidp=np.zeros((480,480,3),dtype=np.uint8)

'''cv.createTrackbar( low_h_name,threshold_window , low_h, max_val_h, nothing)
cv.createTrackbar( high_h_name,threshold_window , high_h, max_val_h, nothing)
cv.createTrackbar( low_s_name,threshold_window , low_s, max_val, nothing)
cv.createTrackbar( high_s_name,threshold_window , high_s, max_val, nothing)
cv.createTrackbar( low_v_name,threshold_window , low_v, max_val, nothing)
cv.createTrackbar( high_v_name,threshold_window , high_v, max_val, nothing)'''
val=0
x=0
y=0
while True:
	try:

		
		mat,frame=cam.read()
		frame = cv.flip(frame,1)
		i_img=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
		if val==0:
			vidp=np.ones_like(frame)*255
			val=1
		'''l_h=cv.getTrackbarPos(low_h_name,threshold_window)
		h_h=cv.getTrackbarPos(high_h_name,threshold_window)
		l_s=cv.getTrackbarPos(low_s_name,threshold_window)
		h_s=cv.getTrackbarPos(high_s_name,threshold_window)
		l_v=cv.getTrackbarPos(low_v_name,threshold_window)
		h_v=cv.getTrackbarPos(high_v_name,threshold_window)'''

		mini=np.array([30,202,107])
		maxi=np.array([180,255,255])
		threshold=cv.inRange(i_img,mini,maxi)
		contours,im2= cv.findContours(threshold, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
		if len(contours)>0:
			cnt=max(contours,key=cv.contourArea)
			'''contours_poly=[None]*len(contours)
			boundRect = [None]*len(contours)
			centers = [None]*len(contours)
			radius = [None]*len(contours)
			for i, c in enumerate(contours):
				contours_poly[i] = cv.approxPolyDP(c, 3, True)'''
				#boundRect[i] = cv.boundingRect(contours_poly[i])
			centers, radius = cv.minEnclosingCircle(cnt)
				
			drawing = np.zeros((threshold.shape[0], threshold.shape[1], 3), dtype=np.uint8)
				
			#for i in range(len(contours)):
			color = (255, 0, 0)
			#cv.drawContours(drawing, contours_poly, i, color)
			'''cv.rectangle(drawing, (int(boundRect[i][0]), int(boundRect[i][1])), \
			(int(boundRect[i][0]+boundRect[i][2]), int(boundRect[i][1]+boundRect[i][3])), color, 2)'''
			cv.circle(drawing, (int(centers[0]), int(centers[1])), int(radius), color, 2)
			cv.circle(drawing,(int(centers[0]), int(centers[1])),5,color,2)

			if x==0 and  y==0:
				cv.line(vidp,(int(centers[0]),int(centers[1])),(int(x),int(y)),color,8,np.uint8)
			x=int(centers[0])
			y=int(centers[1])
			    	

			cv.imshow('Contours', drawing)
			cv.imshow('virtual',vidp)	


			
				

			#cv.imshow("og image",frame)
			#cv.imshow("threshold",threshold)


			key=cv.waitKey(1)
			if key==27:
				break
		else:
			x=0
			y=0
	except:
		pass
	
cam.release()
cv.destroyAllWindows()