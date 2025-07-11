import cv2
import numpy as np
import matplotlib.pyplot as plt

#入力画像読み込み
img_color = cv2.imread("./choco.webp")
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

#ガンマ(教科書と統一した)
gamma_list = [3.0, 2.0, 1.5, 1.0, 0.66, 0.5, 0.33]

#画像ごとに処理して保存＋表示
plt.figure(figsize=(14, 6))
for i, gamma in enumerate(gamma_list):
    inv_gamma = 1.0 / gamma
    
    #γ変換ルックアップテーブル生成
    lut = np.array([255 * ((x / 255) ** inv_gamma) for x in range(256)]).astype("uint8")
    gamma_img = cv2.LUT(img_gray, lut)

    #画像保存
    filename = f"gamma_gray_{gamma:.2f}.jpg"
    cv2.imwrite(filename, gamma_img)

    #表示
    plt.subplot(2, 4, i + 1)
    plt.imshow(gamma_img, cmap='gray')
    plt.title(f"γ = {gamma}")
    plt.axis("off")

plt.tight_layout()
plt.savefig("gamma_gray_all.jpg", dpi=150)
plt.show()
