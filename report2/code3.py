import cv2

# クリック時のコールバック関数
def on_mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Clicked position → x={x}, y={y}")

def main():
    IMG_PATH = "MyAvatar.png"
    # 画像読み込み
    img = cv2.imread(IMG_PATH)
    if img is None:
        print(f"[Error] Failed to load image: {IMG_PATH}")
        return

    # ウィンドウ作成
    winname = "課題3 - Click Pixel Position"
    cv2.namedWindow(winname)
    # コールバック登録
    cv2.setMouseCallback(winname, on_mouse_click)

    # メインループ
    while True:
        cv2.imshow(winname, img)
        # Escキーで終了
        if cv2.waitKey(20) & 0xFF == 27:
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
