import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('test.jpg',0)
edges = cv2.Canny(img,100,200)
print edges.shape
cv2.imwrite('edge.jpg',edges)
tfive = 0
notblack = [0,0,0]
for i in (xrange(0,400)):
    for j in (xrange(0,900)):
        
        if(edges[i,j] > 0):
            notblack.append([i,j])
            tfive = tfive + 1
            print notblack[tfive-1]
print tfive

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()
