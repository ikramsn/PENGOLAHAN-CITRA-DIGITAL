import imageio.v3 as img
import numpy as np
import matplotlib.pyplot as plt

def localTresh(image, block_size, c):
    imgPad = np.pad(image, pad_width=1, mode='constant', constant_values=0)
    threshold = np.zeros_like(image)
    
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            local_area = imgPad[i:i+block_size, j:j+block_size]
            local_mean = np.mean(local_area)
            threshold[i, j] = 255 if image[i][j] > (local_mean - c) else 0
    return threshold

def sobel_edge_detection(image):
    # Definisi kernel Sobel
    sobel_x = np.array([[-1, 0, 1],
                       [-2, 0, 2],
                       [-1, 0, 1]])
    
    sobel_y = np.array([[-1, -2, -1],
                        [0, 0, 0],
                        [1, 2, 1]])
    
    # Konversi gambar ke grayscale jika berwarna
    if len(image.shape) == 3:
        image = np.mean(image, axis=2)
    
    # Padding gambar
    pad_width = 1
    padded = np.pad(image, pad_width, mode='edge')
    
    # Inisialisasi output
    gradient_magnitude = np.zeros_like(image)
    
    # Aplikasikan operator Sobel
    for i in range(pad_width, padded.shape[0]-pad_width):
        for j in range(pad_width, padded.shape[1]-pad_width):
            # Ambil region 3x3
            region = padded[i-1:i+2, j-1:j+2]
            # Hitung gradien
            gx = np.sum(region * sobel_x)
            gy = np.sum(region * sobel_y)
            # Hitung magnitude
            gradient_magnitude[i-1, j-1] = np.sqrt(gx**2 + gy**2)
    
    # Normalisasi ke range 0-255
    gradient_magnitude = (gradient_magnitude / np.max(gradient_magnitude) * 255).astype(np.uint8)
    return gradient_magnitude

# Baca gambar
image1 = img.imread("D:\\Ikram\\Kuliah\\Semester 5\\Pengolahan Citra Digital\\PCD11\\anjing.jpg", mode='F')
image2 = img.imread("D:\\Ikram\\Kuliah\\Semester 5\\Pengolahan Citra Digital\\PCD11\\anjing.jpg")

# Aplikasikan Sobel edge detection
sobel_edges = sobel_edge_detection(image1)

# Aplikasikan local thresholding
thres = localTresh(image1, 15, 10)
mask = (thres == 255).astype(np.uint8)
segmented = image2 * mask[:,:,np.newaxis]

# Tampilkan hasil
plt.figure(figsize=(15, 5))

plt.subplot(2, 3, 1)
plt.imshow(image1, cmap='gray')
plt.title('Gambar Original')

plt.subplot(2, 3, 2)
plt.imshow(sobel_edges, cmap='gray')
plt.title('Deteksi Tepi Sobel')

plt.subplot(2, 3, 3)
plt.imshow(thres, cmap='gray')
plt.title('Local Thresholding')

plt.subplot(2, 3, 4)
plt.imshow(segmented)
plt.title('Hasil Segmentasi')

plt.tight_layout()
plt.show()