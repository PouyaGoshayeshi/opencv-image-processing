import cv2
import numpy as np
from pathlib import Path


# Find the folder containing this Python file
folder = Path(__file__).resolve().parent

# Input image path
image_path = folder / "tamrin3.jpg"

# Read the colour image
image = cv2.imread(str(image_path))

if image is None:
    raise FileNotFoundError(f"Image not found: {image_path}")


# Convert the image from BGR to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV).astype(np.float32)

hue, saturation, value = cv2.split(hsv)

# Scale the Value channel to the range 0–1
value /= 255.0

# Gamma value
gamma = 2.2

# Apply gamma correction
corrected_value = np.power(value, 1.0 / gamma)

# Normalise the corrected values
minimum = corrected_value.min()
maximum = corrected_value.max()

scaled_value = (
    corrected_value - minimum
) / (maximum - minimum + 1e-8)

# Convert back to the range 0–255
final_value = np.round(scaled_value * 255).astype(np.uint8)

# Merge the HSV channels
final_hsv = cv2.merge([
    hue.astype(np.uint8),
    saturation.astype(np.uint8),
    final_value
])

# Convert the result back to BGR
result = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)

# Save the result beside the Python file
output_path = folder / "gamma_corrected.jpg"
cv2.imwrite(str(output_path), result)

print(f"Output saved to: {output_path}")


# Display the original and corrected images
cv2.imshow("Original Image", image)
cv2.imshow(f"Gamma Corrected (gamma={gamma})", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
