import cv2

# 画像を先に読み込んでグローバル変数にしておく
IMG_PATH = "MyAvatar.png"
img = cv2.imread(IMG_PATH)
if img is None:
    print(f"[Error] 画像が読み込めませんでした：{IMG_PATH}")
    exit(1)

# マウスコールバック関数
def on_mouse_click(event, x, y, flags, param):
    # 左ボタンシングルクリックで座標と画素値(BGR)を表示
    if event == cv2.EVENT_LBUTTONDOWN:
        b, g, r = img[y, x]
        print(f"Clicked at ({x}, {y}) → B={b}, G={g}, R={r}")

# ウィンドウ作成とコールバック登録
winname = "課題4 - Pixel Value"
cv2.namedWindow(winname)
cv2.setMouseCallback(winname, on_mouse_click)

# メインループ
while True:
    cv2.imshow(winname, img)
    # Escキーで終了
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()