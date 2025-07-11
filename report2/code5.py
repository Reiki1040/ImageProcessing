import cv2
import sys

def main():
    IMG_PATH = "MyAvatar.png" 

    # 画像読み込み
    img = cv2.imread(IMG_PATH)
    if img is None:
        print(f"[Error] 画像が読み込めませんでした: {IMG_PATH}")
        sys.exit(1)

    # 形状を取得（height, width, channels）
    height, width = img.shape[:2]
    print(f"Image size → width: {width}, height: {height}")

    # 確認用にウィンドウ表示（Escキーで閉じる）
    win = "課題5 - Image Size"
    cv2.namedWindow(win)
    cv2.imshow(win, img)
    while True:
        if cv2.waitKey(20) & 0xFF == 27:
            break
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
