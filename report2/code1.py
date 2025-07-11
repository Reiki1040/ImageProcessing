import cv2

IMG_PATH = "./MyAvatar.png"

img = cv2.imread(IMG_PATH)
cv2.imshow("1) Display Image A", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
