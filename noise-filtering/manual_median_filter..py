import cv2
import numpy as np
from pathlib import Path


# Folder containing this Python file
folder = Path(__file__).resolve().parent

# Input image path
image_path = folder / "tamrin4.jpg"

# Read image in grayscale
image = cv2.imread(str(image_path), cv2.IMREAD_GRAYSCALE)

if image is None:
    raise FileNotFoundError(f"Image not found: {image_path}")


# Median filter settings
kernel_size = 3
padding = kernel_size // 2

# Add reflected padding around the image
padded_image = np.pad(image, padding, mode="reflect")

# Create an empty output image
filtered_image = np.zeros_like(image)


# Apply the median filter manually
for row in range(image.shape[0]):
    for column in range(image.shape[1]):
        region = padded_image[
            row: row + kernel_size,
            column: column + kernel_size
        ]

        filtered_image[row, column] = np.median(region)


# Save the result beside the Python file
output_path = folder / "median_filtered.jpg"
cv2.imwrite(str(output_path), filtered_image)

print(f"Output saved to: {output_path}")


# Display original and filtered images
cv2.imshow("Original Image", image)
cv2.imshow(
    f"Median Filter {kernel_size}x{kernel_size}",
    filtered_image
)

cv2.waitKey(0)
cv2.destroyAllWindows()
