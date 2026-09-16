import cv2
import numpy as np
img = cv2.imread('tamrin3.jpg')
# تبدیل به HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV).astype(np.float32)
h, s, v = cv2.split(hsv)

# مقیاس 0-1
v /= 255.0

# مقدار گاما
gamma = 2.2
v_corrected = np.power(v, 1.0 / gamma)

#  کمترین مثدار صفر بیشترین 1مقیاس‌بندی 
min_val = v_corrected.min()
max_val = v_corrected.max()
v_scaled = (v_corrected - min_val) / (max_val - min_val + 1e-8)

# بازگرداندن به 0-255
v_final = np.round(v_scaled * 255).astype(np.uint8)

# ترکیب کانال‌ها و بازگشت به BGR
hsv_final = cv2.merge([h.astype(np.uint8), s.astype(np.uint8), v_final])
result = cv2.cvtColor(hsv_final, cv2.COLOR_HSV2BGR)
cv2.imwrite("gamma_corrected.jpg", result)
cv2.imshow('Original', img)
cv2.imshow(f'Gamma corrected (γ={gamma})', result)
cv2.waitKey(0)
cv2.destroyAllWindows()



