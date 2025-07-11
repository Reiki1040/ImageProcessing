import cv2
import numpy as np

# 状態保持用のグローバル変数
drawing = False   # マウス押下中フラグ
ix, iy = -1, -1   # ドラッグ開始位置

# コールバック関数
def draw_rectangle(event, x, y, flags, param):
    global drawing, ix, iy, img
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        # マウスを離した位置(x,y)まで矩形を描画
        cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 255), 2)

# 画像読み込み（JPEG/BMP）
img = cv2.imread("MyAvatar.png")
if img is None:
    raise SystemExit("画像が読み込めませんでした")

# ウィンドウ作成＆コールバック登録
cv2.namedWindow("課題6 - 矩形指定")
cv2.setMouseCallback("課題6 - 矩形指定", draw_rectangle)

# メインループ
while True:
    cv2.imshow("課題6 - 矩形指定", img)
    # Esc キーで終了
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()