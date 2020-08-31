import numpy as np 
import cv2 as cv
indow_name='og image'
threshold_window='threshold '
#reading frames from camera
cam=cv.VideoCapture(0)
#threshold_window='threshold_window'
#cv.namedWindow(threshold_window)
val=0
x=0
y=0
#iterating frames in a loop
while True:
	try:

		#takes 1 frame at a time
		mat,frame=cam.read()
		frame = cv.flip(frame,1)
		i_img=cv.cvtColor(frame,cv.COLOR_BGR2HSV)# converts to hsv
		if val==0:
			vidp=np.ones_like(frame)*255
			val=1
		mini=np.array([30,202,107])#setting hsv values ...here for blue
		maxi=np.array([180,255,255])
		threshold=cv.inRange(i_img,mini,maxi)#finding threshold
		contours,im2= cv.findContours(threshold, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)#finds contours
		if len(contours)>0:
			cnt=max(contours,key=cv.contourArea)#filters contours and takes contours with max area here the object
			centers, radius = cv.minEnclosingCircle(cnt)
				
			drawing = np.zeros((threshold.shape[0], threshold.shape[1], 3), dtype=np.uint8)#tracks the path of the object
			color = (255, 0, 0)
			cv.circle(drawing, (int(centers[0]), int(centers[1])), int(radius), color, 2)#shows the circular object boundary
			cv.circle(vidp,(int(centers[0]), int(centers[1])),5,color,2)

			if x==0 and  y==0:
				x=int(centers[0])   
				y=int(centers[1])
			else:
				cv.line(vidp,(int(centers[0]),int(centers[1])),(int(x),int(y)),color,8)#draws line from center in the current frame to center from previous frame

			x=int(centers[0]) # updates center with current object center
			y=int(centers[1])
			    	
			#cv.imshow("og image",frame) # displays video
			cv.imshow('Contours', drawing) #displays the object and its current position
			cv.imshow('virtual',vidp)	# displays the drawing
			key=cv.waitKey(1)
			if key==27:              #exit command
				break
		else:
			x=0
			y=0
	except:
		pass
	
cam.release()
cv.destroyAllWindows()	