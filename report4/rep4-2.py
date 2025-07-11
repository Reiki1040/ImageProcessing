import cv2
from matplotlib import pyplot as plt

image1_path = "./igo.jpg"           #画像パス指定
image1 = cv2.imread(image1_path,0)      #画像読み込み(0でグレースケール,1でカラー)

image_max = 255 #最大輝度値

# 適応的閾値処理による二値化
image1_binary = cv2.adaptiveThreshold(image1, image_max, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 39, 2)

"""
cv2.threshold()の
第一引数は二値化する画像
第二引数は最大輝度値
第三引数は閾値計算のタイプ
第四引数は閾値処理のタイプ
第五引数は局所領域のサイズ(奇数である必要がある)
第六引数は閾値から引く値
"""

image1_path_output = "./igo.png"            #出力画像のパス
cv2.imwrite(image1_path_output, image1_binary)   #保存

fig = plt.figure()  #グラフのインスタンス化
ax1 = fig.add_subplot(111)

ax1.imshow(image1_binary, cmap = 'gray')
fig.tight_layout()
plt.show()
plt.close()


