import cv2
import numpy as np
from pathlib import Path


def add_salt_pepper_noise(image, amount=0.05):
    noisy_image = image.copy()
    rows, columns = image.shape

    number_of_pixels = int(amount * rows * columns)

    # Add salt noise (white pixels)
    for _ in range(number_of_pixels // 2):
        row = np.random.randint(0, rows)
        column = np.random.randint(0, columns)
        noisy_image[row, column] = 255

    # Add pepper noise (black pixels)
    for _ in range(number_of_pixels // 2):
        row = np.random.randint(0, rows)
        column = np.random.randint(0, columns)
        noisy_image[row, column] = 0

    return noisy_image


# Find the folder containing this Python file
folder = Path(__file__).resolve().parent

# Input image path
image_path = folder / "tamrin4.jpg"

# Read the image in grayscale
image = cv2.imread(str(image_path), cv2.IMREAD_GRAYSCALE)

if image is None:
    raise FileNotFoundError(f"Image not found: {image_path}")


# Add salt-and-pepper noise
noisy_image = add_salt_pepper_noise(image, amount=0.05)

# Save the output beside the Python file
output_path = folder / "noisy_salt_pepper.jpg"
cv2.imwrite(str(output_path), noisy_image)

print(f"Output saved to: {output_path}")


# Display the images
cv2.imshow("Original Image", image)
cv2.imshow("Salt and Pepper Noise", noisy_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
