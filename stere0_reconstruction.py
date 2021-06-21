import cv2
import numpy as np
from matplotlib import pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()



imgL=cv2.imread('recon_l.png')
imgR=cv2.imread('recon_r.png')
#cv2.destroyAllWindows()

#print(image.shape)
doffs=127.471
b=174.019
f=5817.412
window_size2=5
stereo =  cv2.StereoSGBM_create(minDisparity = 38, numDisparities = 181, blockSize = 5, uniquenessRatio = 5, speckleWindowSize = 5, speckleRange = 5, disp12MaxDiff = 0, P1 = 83*window_size2, P2 = 323*window_size2)
disp_map = stereo.compute(imgL,imgR).astype(np.float32)/60
disparity = cv2.pyrDown(disp_map)
image = cv2.pyrDown(cv2.imread('recon_l.png'))


Q = np.array([[1, 0, 0, -2960/2], [0, 1, 0, -2008/2],[0, 0, 0, f],[0, 0, -1/b, doffs/b]])
points = cv2.reprojectImageTo3D(disparity, Q)
print(points.shape)


xp=points[:,:,0]
yp=points[:,:,1]
zp=points[:,:,2]

xp=xp.flatten().reshape(-1,1)

yp=yp.flatten().reshape(-1,1)

zp=zp.flatten().reshape(-1,1)
point3d=np.hstack((xp,yp,zp))
mask = disparity > disparity.min()
#print(mask[0])
colors = image
#cv2.imshow('colors', colors)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

out_points = points[mask]
out_colors = image[mask]

verts = out_points.reshape(-1,3)
colors = out_colors.reshape(-1,3)
verts = np.hstack([verts, colors])

ply_header = '''ply
	format ascii 1.0
	element vertex %(vert_num)d
	property float x
	property float y
	property float z
	property uchar blue
	property uchar green
	property uchar red
	end_header
	'''
with open('output.ply', 'w') as f:
	f.write(ply_header %dict(vert_num = len(verts)))
	np.savetxt(f, verts, '%f %f %f %d %d %d')

print("DONE")
cv2.imshow('disparity', disparity)
cv2.imshow('window', image)
cv2.waitKey(0)
cv2.destroyAllWindows()