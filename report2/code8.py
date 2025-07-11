import cv2
import numpy as np
import glob

def main():
    paths = sorted(glob.glob("images/*.jpg"))[:12]
    imgs = []
    for p in paths:
        img = cv2.imread(p)
        if img is None:
            print(f"Failed to load: {p}")
            return
        imgs.append(img)

    # 全画像を同じサイズにリサイズ
    h, w = imgs[0].shape[:2]
    imgs = [cv2.resize(im, (w, h)) for im in imgs]

    # 4枚ずつ横に連結して 3 行作り、さらに縦に連結
    rows = [np.hstack(imgs[i*4:(i+1)*4]) for i in range(3)]
    grid = np.vstack(rows)

    cv2.imshow("A8) 4x3 Grid", grid)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
