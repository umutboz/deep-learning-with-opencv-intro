import numpy as np
import cv2

img = cv2.imread('../Deep_Learning_OpenCV/images/devon.jpg')
print(type(img))
print("BGR")
print(img.shape)


cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
