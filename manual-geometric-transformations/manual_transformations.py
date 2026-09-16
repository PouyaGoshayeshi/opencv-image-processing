import cv2
import numpy as np
import math

image = cv2.imread("tabdil.jpg")
if image is None:
    print("❌ تصویر پیدا نشد!")
    exit()
    #ارتفاع و عرض رو میگیریم که 2 تا ارایه برای مختصات جدید نگهداری کنه  تابع تبدیل چرخش#
    
def transform_rotation(img):
    h, w = img.shape[:2]
    map_x = np.zeros((h, w), dtype=np.float32)
    map_y = np.zeros((h, w), dtype=np.float32)
    #مقدار ثابت برای چرخش 45 درجه هست را محاسبه و بعد مرکز رو پیدا میکند#
    sqrt2_2 = math.sqrt(2) / 2
    center_x, center_y = w // 2, h // 2
    #رو هرپیکسل در تصویر بررسی میشه و مختصات جدید میگیرن بعد مختصات به مرکز داده میشه بعد میچرخومه45 درجه و  دوباره مختصات رو برمیگرد.نه#
    for y in range(h):
        for x in range(w):
            rel_x = x - center_x
            rel_y = y - center_y
            new_x = sqrt2_2 * rel_x - sqrt2_2 * rel_y
            new_y = sqrt2_2 * rel_x + sqrt2_2 * rel_y
            map_x[y, x] = new_x + center_x
            map_y[y, x] = new_y + center_y
    
    return cv2.remap(img, map_x, map_y, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
#تابع تبدیل موجی  موج فقط در جهت افقی باشه      قدرت موج 20 فرکانس 30   ابعاد  رو میگیره و بعد نقشه های خالی ایجاد میشه #
def transform_wave(img, amplitude=20, frequency=30):
    h, w = img.shape[:2]
    #xمختصات جدید هر پیکسل ایکس رو نگه میداره #
    # y ماله yرو    #
    map_x = np.zeros((h, w), dtype=np.float32)
    map_y = np.zeros((h, w), dtype=np.float32)
    
    for y in range(h):
        for x in range(w):
            map_x[y, x] = x + amplitude * math.sin(2 * math.pi * x / frequency)
            map_y[y, x] = y
    
    return cv2.remap(img, map_x, map_y, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
#اول تصویر میچرخد و بعد رو تصویر چرخیدن شده موجی میشود #
def transform_combined(img, amplitude=15, frequency=25):
    rotated = transform_rotation(img)
    return transform_wave(rotated, amplitude, frequency)

result_rotation = transform_rotation(image)#فقط چرخش#
result_wave = transform_wave(image, amplitude=20, frequency=30)#فقط موج#
result_combined = transform_combined(image, amplitude=15, frequency=25)#موج و چرخش باهم
cv2.imshow("تصویر اصلی", image)
cv2.imshow("تبدیل چرخش", result_rotation)
cv2.imshow("تبدیل موجی", result_wave)
cv2.imshow("تبدیل ترکیبی", result_combined)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("transform_rotation.jpg", result_rotation)
cv2.imwrite("transform_wave.jpg", result_wave)
cv2.imwrite("transform_combined.jpg", result_combined)  
