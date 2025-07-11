import cv2

img1 = cv2.imread("umi.jpg")
img2 = cv2.imread("sakana.jpg")
#リサイズ
img1 = cv2.resize(img1, (512, 512))
img2 = cv2.resize(img2, (512, 512))

#αを設定
alpha = 0.6
#αブレンディング
blended = cv2.addWeighted(img1, alpha, img2, 1 - alpha, 0)

cv2.imwrite("alpha_fixed.jpg", blended)
cv2.imshow("Fixed Alpha Blending", blended)
cv2.waitKey(0)
cv2.destroyAllWindows()
