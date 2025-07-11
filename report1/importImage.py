import cv2

img = cv2.imread("report1/testImage.jpg.webp")
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()