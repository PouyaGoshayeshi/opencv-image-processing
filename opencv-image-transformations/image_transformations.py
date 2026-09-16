import cv2
import numpy as np
import os
print("📁 مسیر فعلی اجرای برنامه:", os.getcwd())


image = cv2.imread(r"tabdil.jpg")  
if image is None:
    print(" تصویر پیدا نشد! مسیر فایل را بررسی کن.")
    exit()

def rotate_image(img, angle=45):
    h, w = img.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    cos_val = np.abs(M[0, 0])
    sin_val = np.abs(M[0, 1])
    new_w = int((h * sin_val) + (w * cos_val))
    new_h = int((h * cos_val) + (w * sin_val))

    M[0, 2] += (new_w / 2) - center[0]
    M[1, 2] += (new_h / 2) - center[1]

    rotated = cv2.warpAffine(img, M, (new_w, new_h), borderMode=cv2.BORDER_REFLECT)
    return rotated


def wave_distortion(img, amplitude=20, frequency=30):
   
    h, w = img.shape[:2]

    
    x = np.arange(w)
    y = np.arange(h)
    x_map, y_map = np.meshgrid(x, y)

   
    x_map = x_map + amplitude * np.sin(2 * np.pi * y_map / frequency)

    x_map = x_map.astype(np.float32)
    y_map = y_map.astype(np.float32)
    waved = cv2.remap(img, x_map, y_map, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
    return waved

rotated = rotate_image(image, 45)                 
waved = wave_distortion(image, amplitude=25, frequency=40)


cv2.imwrite("rotated_output.jpg", rotated)
cv2.imwrite("waved_output.jpg", waved)

cv2.imshow("tabdil.jpg", image)
cv2.imshow("🔄 چرخش 45 درجه‌ای", rotated)
cv2.imshow("🌊 اعوجاج موجی نرم", waved)

cv2.waitKey(0)
cv2.destroyAllWindows()

