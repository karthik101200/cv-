## DEPTH,DISPARITY MAPS and VIRTUAL DRAWING PAD

A depth map is very similar to the heat map that we often see 

Here the purpose is to observe the difference in depth of each object(or rather pixel) from the camera. As we know a single image lacks the 3rd dimension of depth (2D image).
Thus we need two images from the same camera(stereo pair) so that we use it to find the 3rd dimension

<img src ="https://user-images.githubusercontent.com/64783286/120322690-50ed1e00-c302-11eb-99c5-71dd539a5524.png" width="250" height="250" />

Disparity map on the other hand the pixel difference between the stereo pair and is shown below

Left and Right images


<img src ="https://user-images.githubusercontent.com/64783286/120323049-b3deb500-c302-11eb-9cbd-3368beff3aa5.png" width="250" height="250" />   <img src ="https://user-images.githubusercontent.com/64783286/120323662-58f98d80-c303-11eb-8799-6e921f1f2b2e.png" width="250" height="250" />

Disparity Map:

<img src ="https://user-images.githubusercontent.com/64783286/120324066-d02f2180-c303-11eb-9c04-3b8e903b2921.png" width="250" height="250" />

Depth Map:

<img src ="https://user-images.githubusercontent.com/64783286/120323868-965e1b00-c303-11eb-9660-d399a7ee2cb6.png" width="250" height="250" />

# VIRTUAL DRAWING PAD:
Virtual darwing pad uses an object preferrably sysmtrric and small like bottle or pen cap and tracks it and draws these tracks on a window

It does this by eleminating the backgraound and drwaing a contour around this object and tracks it centre or centroid

