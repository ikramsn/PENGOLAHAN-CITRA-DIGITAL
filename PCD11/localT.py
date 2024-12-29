import imageio.v3 as img
import numpy as np
import matplotlib.pyplot as plt

def localTresh(image, block_size, c):
    imgPad = np.pad(image, pad_width=block_size // 2, mode='constant', constant_values=0)
    threshold = np.zeros_like(image)
    
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            local_area = imgPad[i:i+block_size, j:j+block_size]
            local_mean = np.mean(local_area)
            threshold[i, j] = 255 if image[i, j] > (local_mean - c) else 0
    return threshold

# Load grayscale and color images
image1 = img.imread("D:\\Ikram\\Kuliah\\Semester 5\\Pengolahan Citra Digital\\PCD11\\anjing.jpg", mode='F')
image2 = img.imread("D:\\Ikram\\Kuliah\\Semester 5\\Pengolahan Citra Digital\\PCD11\\anjing.jpg")

thres = localTresh(image1, 15, 10)
mask = (thres == 255).astype(np.uint8)

# Apply mask to each channel of image2
segmented = image2 * mask[:, :, np.newaxis]

plt.figure(figsize=(10, 6))

plt.subplot(2, 3, 1)
plt.imshow(image1, cmap='gray')
plt.title("Original Grayscale")

plt.subplot(2, 3, 2)
plt.imshow(thres, cmap='gray')
plt.title("Thresholded")

plt.subplot(2, 3, 3)
plt.imshow(segmented)
plt.title("Segmented Image")

plt.show()
