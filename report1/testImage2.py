import cv2
import numpy as np

img = np.zeros((500, 500, 3), dtype=np.uint8)

cv2.line(img, (50, 50), (450, 50), (255, 0, 0), 3)
cv2.rectangle(img, (50, 100), (200, 200), (0, 255, 0), -1)
cv2.circle(img, (300, 300), 50, (0, 0, 255), -1)
cv2.putText(img, "Hello OpenCV", (100, 400),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

cv2.imshow("Drawing", img)
cv2.waitKey(0)
cv2.destroyAllWindows()