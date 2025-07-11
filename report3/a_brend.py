import cv2
import numpy as np

img1 = cv2.imread("umi.jpg")
img2 = cv2.imread("sakana.jpg")
img1 = cv2.resize(img1, (512, 512))
img2 = cv2.resize(img2, (512, 512))
h, w = img1.shape[:2]

result = np.zeros_like(img1)

#横方向にα値をグラデーションで変化（左から右）
for x in range(w):
    a = x / w
    result[:, x] = cv2.addWeighted(img1[:, x], a, img2[:, x], 1 - a, 0)

cv2.imwrite("alpha_gradient.jpg", result)
cv2.imshow("Gradient Alpha Blending", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
