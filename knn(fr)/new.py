import cv2
img=cv2.imread('dog1.png')
#new=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
cv2.imshow('dog image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()