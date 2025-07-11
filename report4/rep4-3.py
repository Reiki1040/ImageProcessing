import cv2
from matplotlib import pyplot as plt

img = cv2.imread('WL.png', 0) #グレースケールで画像読み込み
 
#二値化
ret, img_binary = cv2.threshold(img,70, 255,cv2.THRESH_BINARY)

#輪郭抽出
contours, hierarchy = cv2.findContours(img_binary,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)

#輪郭を元画像に描画
img_contour = cv2.drawContours(img, contours, -1, (0, 255, 0), 5)
 
#画像描画
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.imshow(cv2.cvtColor(img_contour, cv2.COLOR_BGR2RGB))
ax1.axis('off')
plt.show()
plt.close()