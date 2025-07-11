import cv2
import numpy as np
import glob

# 定数
RESIZE_TO = (300, 300)

# 画像読み込みとリサイズ
paths = sorted(glob.glob("images/*.jpg"))[:12]
imgs = []

for p in paths:
    img = cv2.imread(p)
    if img is None:
        print(f"Failed to load: {p}")
        continue
    img = cv2.resize(img, RESIZE_TO)
    imgs.append(img)

# 配置情報 (x0, y0, x1, y1)
positions = [
    (j * RESIZE_TO[0], i * RESIZE_TO[1], (j + 1) * RESIZE_TO[0], (i + 1) * RESIZE_TO[1])
    for i in range(3) for j in range(4)
]

clicks = []  # 選択された画像のインデックス（最大2）

# 描画関数（赤枠表示付き）
def update_grid():
    # グリッド画像を一時的に結合
    rows = [np.hstack(imgs[i*4:(i+1)*4]) for i in range(3)]
    grid = np.vstack(rows)

    # 赤枠を描画（選択中の画像）
    for idx in clicks:
        x0, y0, x1, y1 = positions[idx]
        cv2.rectangle(grid, (x0, y0), (x1, y1), (0, 0, 255), 5)

    cv2.imshow("A10) Swap Two (with highlight)", grid)

def on_click(event, x, y, flags, param):
    global clicks
    if event == cv2.EVENT_LBUTTONDOWN:
        for idx, (x0, y0, x1, y1) in enumerate(positions):
            if x0 <= x < x1 and y0 <= y < y1:
                if idx not in clicks:
                    clicks.append(idx)
                    print(f"Selected: {idx}")

                if len(clicks) == 2:
                    i, j = clicks
                    imgs[i], imgs[j] = imgs[j], imgs[i]
                    clicks = []  # 入れ替え後、選択をクリア
                update_grid()
                break

def main():
    if len(imgs) != 12:
        print("画像が12枚揃っていません")
        return

    cv2.namedWindow("A10) Swap Two (with highlight)")
    cv2.setMouseCallback("A10) Swap Two (with highlight)", on_click)
    update_grid()
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
