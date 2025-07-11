import cv2
import numpy as np
from matplotlib import pyplot as plt

image_path = "syake_image.webp"           #画像パス指定
image = cv2.imread(image_path,0)      #画像読み込み(0でグレースケール,1でカラー)
image_color = cv2.imread(image_path,1) 

#ガウシアンフィルタ3x3でノイズ除去
blur = cv2.GaussianBlur(image, (3, 3), sigmaX=1)

#Cannyエッジ検出で輪郭抽出
edges = cv2.Canny(blur, threshold1=100, threshold2=200)

#輪郭の追跡
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#元画像に輪郭を描画
cv2.drawContours(image_color, contours, -1, (0, 255, 0), 2)

image_path_output = "./syake_contours.png" #出力画像のパス
cv2.imwrite(image_path_output, image_color)  #保存

plt.subplot(1, 3, 3)
plt.title("Contours")
plt.imshow(cv2.cvtColor(image_color, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.tight_layout()
plt.show()
