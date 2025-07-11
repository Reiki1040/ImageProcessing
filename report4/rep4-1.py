import cv2
from matplotlib import pyplot as plt

image1_path = "./igo.jpg"           #画像パス指定
image1 = cv2.imread(image1_path,0)      #画像読み込み(0でグレースケール,1でカラー)

th = 120 #閾値
image_max = 255 #最大輝度値
ret, image1_binary = cv2.threshold(image1, th, image_max, cv2.THRESH_BINARY) #二値化処理

"""
cv2.threshold()の
第一引数はグレースケール画像
第二引数は閾値
第三引数は最大輝度値
第四引数は二値タイプ

この関数の第一戻り値は閾値がかえってくる
"""
image1_path_output = "./igo.png"            #出力画像のパス
cv2.imwrite(image1_path_output, image1_binary)   #保存

fig = plt.figure()  #グラフのインスタンス化
ax1 = fig.add_subplot(111)

ax1.imshow(image1_binary, cmap = 'gray')
fig.tight_layout()
plt.show()
plt.close()


