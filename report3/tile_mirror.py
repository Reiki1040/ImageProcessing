import cv2
import numpy as np
import time

img = cv2.imread("choco.webp")

#サイズを3×3タイルで割り切れるように調整
h, w = img.shape[:2]
tile_h = h // 3
tile_w = w // 3
img = cv2.resize(img, (tile_w * 3, tile_h * 3))  #リサイズ

#タイルを左上から順番に反転
for i in range(3):
    for j in range(3):
        y1, y2 = i * tile_h, (i + 1) * tile_h
        x1, x2 = j * tile_w, (j + 1) * tile_w

        print(f"反転中：({i}, {j}) タイル")
        tile = img[y1:y2, x1:x2]
        flipped_tile = cv2.flip(tile, 1)  #左右反転

        img[y1:y2, x1:x2] = flipped_tile

        cv2.imshow("Mosaic Flip Sequential", img)
        cv2.waitKey(5000) 

cv2.destroyAllWindows()
cv2.imwrite("mosaic_sequential.jpg", img)
