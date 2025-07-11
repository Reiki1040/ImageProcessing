import cv2
import time
import glob

def main():
    paths = sorted(glob.glob("images/*.jpg"))[:12]
    if len(paths) < 12:
        print("Error: images フォルダに12枚の JPEG 画像を用意してください")
        return

    for p in paths:
        img = cv2.imread(p)
        if img is None:
            print(f"Failed to load: {p}")
            continue
        cv2.imshow("A7) Slideshow", img)
        # waitKeyを分割しないとキー入力が効かないので先に一瞬呼び出す
        cv2.waitKey(1)
        time.sleep(6)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
