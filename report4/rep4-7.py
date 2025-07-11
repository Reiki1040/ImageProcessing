import numpy as np
import cv2

def lowpass_filter(src, sigma=0.5):
    
    src = np.fft.fft2(src)
    height, width = src.shape
    cy, cx = int(height / 2), int(width / 2)

    fsrc = np.fft.fftshift(src)

    y, x = np.ogrid[:height, :width]
    mask = np.exp(-((x - cx)**2 + (y - cy)**2) / (2 * (sigma * min(height, width) / 2)**2))

    fdst = fsrc * mask
    fdst = np.fft.ifftshift(fdst)
    dst = np.fft.ifft2(fdst)

    dst_real = np.real(dst)
    dst_normalized = cv2.normalize(dst_real, None, 0, 255, cv2.NORM_MINMAX)

    return dst_normalized.astype(np.uint8)

def main():
    # ガウス分布のパラメータ（小さいほどフィルタの影響が強くなる)
    sigma = 0.3

    # 入力画像を読み込み
    img = cv2.imread("syake_image.webp")

    # RGB画像をRed, Green, Blueの1チャンネル画像に分割
    img_blue, img_green, img_red = cv2.split(img)

    # ローパスフィルタ処理
    himg_blue = lowpass_filter(img_blue, sigma)
    himg_green = lowpass_filter(img_green, sigma)
    himg_red = lowpass_filter(img_red, sigma)

    # RGB画像に戻す
    himg = cv2.merge((himg_blue, himg_green, himg_red))

    # 処理結果を出力
    cv2.imwrite("syake_lowpass_filter.png", himg)

if __name__ == "__main__":
    main()