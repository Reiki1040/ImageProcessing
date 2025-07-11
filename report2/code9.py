import cv2
import numpy as np
import glob

#読み込み
paths = sorted(glob.glob("images/*.jpg"))[:12]
imgs = []


RESIZE_TO = (300, 300)

for p in paths:
    img = cv2.imread(p)
    if img is None:
        print(f"Failed to load: {p}")
        continue
    img = cv2.resize(img, RESIZE_TO)
    imgs.append(img)

positions = [
    (j * RESIZE_TO[0], i * RESIZE_TO[1], (j+1) * RESIZE_TO[0], (i+1) * RESIZE_TO[1])
    for i in range(3) for j in range(4)
]

def update_grid():
    rows = [np.hstack(imgs[i*4:(i+1)*4]) for i in range(3)]
    grid = np.vstack(rows)
    cv2.imshow("A9) Remove One", grid)

def on_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        for idx, (x0, y0, x1, y1) in enumerate(positions):
            if x0 <= x < x1 and y0 <= y < y1:
                # 選択した画像を白で塗り潰す
                imgs[idx][:] = 255
                update_grid()
                break

def main():
    if len(imgs) != 12:
        print("画像が12枚揃っていません")
        return

    cv2.namedWindow("A9) Remove One")
    cv2.setMouseCallback("A9) Remove One", on_click)
    update_grid()
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
