import cv2
import numpy as np

def on_mouse_move(event, x, y, flags, param):
    """マウス移動時に座標をコンソール出力"""
    if event == cv2.EVENT_MOUSEMOVE:
        print(f"x={x}, y={y}")

def main():
    # 画面全体に広げるダミー画像
    img = np.zeros((512, 512, 3), dtype=np.uint8)
    winname = "screen"

    # ウィンドウを作成 & フルスクリーン化
    cv2.namedWindow(winname, cv2.WINDOW_NORMAL)
    cv2.setWindowProperty(winname, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    # マウスコールバック登録
    cv2.setMouseCallback(winname, on_mouse_move)

    # 最初に一度だけ表示
    cv2.imshow(winname, img)

    # Esc が押されるまで待機ループ
    while True:
        if cv2.waitKey(20) & 0xFF == 27:  # 27==Esc
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
