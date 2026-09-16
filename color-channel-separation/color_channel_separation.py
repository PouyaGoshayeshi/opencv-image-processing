import cv2
import numpy as np
from pathlib import Path


# Find the folder containing this Python file
folder = Path(__file__).resolve().parent

# Input image
image_path = folder / "tabdil.jpg"
image = cv2.imread(str(image_path))

if image is None:
    raise FileNotFoundError(f"Image not found: {image_path}")


# OpenCV reads colour images in BGR format
blue, green, red = cv2.split(image)

zeros = np.zeros_like(blue)

# Create individual colour-channel images
blue_image = cv2.merge([blue, zeros, zeros])
green_image = cv2.merge([zeros, green, zeros])
red_image = cv2.merge([zeros, zeros, red])

# Merge all channels again
merged_image = cv2.merge([blue, green, red])


# Save outputs
cv2.imwrite(str(folder / "blue_channel.jpg"), blue_image)
cv2.imwrite(str(folder / "green_channel.jpg"), green_image)
cv2.imwrite(str(folder / "red_channel.jpg"), red_image)
cv2.imwrite(str(folder / "merged_image.jpg"), merged_image)


# Display results
cv2.imshow("Original Image", image)
cv2.imshow("Blue Channel", blue_image)
cv2.imshow("Green Channel", green_image)
cv2.imshow("Red Channel", red_image)
cv2.imshow("Merged Image", merged_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
