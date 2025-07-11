import cv2

img = cv2.imread("sakana.jpg")
#左右反転（flipCode = 1）
flipped_img = cv2.flip(img, 1)

cv2.imshow("Original", img)
cv2.imshow("Flipped", flipped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("flipped_image.jpg", flipped_img)
