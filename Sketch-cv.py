import cv2

img =cv2.imread("butterfly.jpg")

imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_neg = cv2.bitwise_not(imgGray)
imgBlur=cv2.GaussianBlur(img_neg,(21,21),0)
invertedblur = 255 - imgBlur
sketch = cv2.divide(imgGray, invertedblur)

cv2.imshow("original", img)
cv2.waitKey(0)
cv2.imshow("invertedblur", invertedblur)
cv2.waitKey(0)
cv2.imshow("sketch", sketch)
cv2.waitKey(0)