import numpy as np
import cv2

img = cv2.imread('../Deep_Learning_OpenCV/images/devon.jpg')
print("BGR")

print("blue channel values")
b = img[:,:,0]
print(b)

'''
print("green channel values")
g = img[:,:,1]
print(g)
'''

'''
print("red channel values")
r = img[:,:,2]
print(r)
'''

cv2.imshow('Blue',b)
cv2.imshow('Green',g)
cv2.imshow('Red',r)
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
