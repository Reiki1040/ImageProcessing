import cv2
import numpy as np
import matplotlib.pyplot as plt

#カラー画像の読み込み
img_color = cv2.imread("choco.webp")
img_color = cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB)

#チャンネルごとに異なるγ値を設定
gamma_r = 1.8  #赤
gamma_g = 0.7  #緑
gamma_b = 0.4  #青

#ルックアップテーブル作成
def create_lut(gamma):
    return np.array([255 * ((x / 255) ** (1.0 / gamma)) for x in range(256)]).astype("uint8")

lut_r = create_lut(gamma_r)
lut_g = create_lut(gamma_g)
lut_b = create_lut(gamma_b)

r, g, b = cv2.split(img_color)
r_corr = cv2.LUT(r, lut_r)
g_corr = cv2.LUT(g, lut_g)
b_corr = cv2.LUT(b, lut_b)

img_fantasy = cv2.merge([r_corr, g_corr, b_corr])

cv2.imwrite("gamma_color_fantasy.jpg", cv2.cvtColor(img_fantasy, cv2.COLOR_RGB2BGR))
plt.imshow(img_fantasy)
plt.title("(R=1.8, G=0.7, B=0.4)")
plt.axis("off")
plt.show()
