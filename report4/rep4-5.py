import cv2
from matplotlib import pyplot as plt

image1_path = "syake_image.webp"   #画像パス指定
image1 = cv2.imread(image1_path,0) #画像読み込み(0でグレースケール,1でカラー)

def unsharp_masking(img, kx, ky, k):
    img_copy = img.astype('int16').copy() #符号付き16bit整数に変換してコピー
    img_gaussian = cv2.GaussianBlur(img_copy, (kx, ky) ,sigmaX=1) #ガウシアンフィルタ(3x3)で画像をぼかす
    diff_img = img_copy -img_gaussian   #元画像とぼかし画像の差分を計算
    img_k = diff_img * k   #差分に k を掛けて、どれだけ強調するかを調整
    result = img_copy + img_k
    return result

image1_unsharp_masked = unsharp_masking(image1, 3, 3, 100)

image1_path_output = "./syake_unsharp_masked_3x3_k=100.png" #出力画像のパス
cv2.imwrite(image1_path_output, image1_unsharp_masked)  #保存

fig = plt.figure()  #グラフのインスタンス化
ax1 = fig.add_subplot(111)

ax1.imshow(image1_unsharp_masked, cmap = 'gray')
fig.tight_layout()
plt.show()
plt.close()


