import cv2

origin = cv2.imread('media/limf.JPG')

# img = cv2.resize(img, (img.shape[1] // 2, img.shape [0] // 2))
blur = cv2.GaussianBlur(origin,(5,5), 0)
img = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)

img = cv2.Canny(img, 90,90)
cv2.imshow('Result', img)
cv2.imshow('Blur', blur)
cv2.imshow('Original image', origin)


cv2.waitKey(0)
