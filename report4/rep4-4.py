import cv2
from matplotlib import pyplot as plt
import numpy as np
from IPython.display import Image, display

img = cv2.imread("./syake_image.webp")

filter_image = cv2.blur(img, (5, 5)) #5x5の平均化フィルタをかける

image1_path_output = "./syake_filter5x5.png"        #出力画像のパス
cv2.imwrite(image1_path_output, filter_image)       #保存

fig = plt.figure()  #グラフのインスタンス化
ax1 = fig.add_subplot(111)

ax1.imshow(filter_image, cmap = 'gray')
fig.tight_layout()
plt.show()
plt.close()