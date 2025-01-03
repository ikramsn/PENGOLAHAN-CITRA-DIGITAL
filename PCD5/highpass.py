import imageio.v3 as image
import numpy as np
import matplotlib.pyplot as plt

# Path ke citra yang akan diproses
path = "D:\\Ikram\\Kuliah\\Semester 5\\Pengolahan Citra Digital\\PCD5\\Picture\\view.jpg"

# Membaca citra
my_image = image.imread(path)

# Fungsi untuk mengonversi citra berwarna ke grayscale
def convert_to_grey(image):
    red = image[:, :, 0]
    green = image[:, :, 1]
    blue = image[:, :, 2]
    grey = (red + green + blue) / 3  # Menghitung rata-rata intensitas
    return grey  # Kembalikan citra grayscale sebagai 2D array (bukan 3D)

# Fungsi untuk menerapkan filter low-pass pada citra grayscale
def low_pass_filter_grayscale(image):
    filtered_image = np.zeros_like(image)
    for i in range(1, image.shape[0] - 1):  # Iterasi untuk setiap piksel (menghindari batas citra)
        for j in range(1, image.shape[1] - 1):
            filtered_image[i, j] = np.mean(image[i-1:i+2, j-1:j+2])  # Mengambil 3x3 area dan menghitung rata-rata
    return filtered_image

# Fungsi untuk menerapkan filter low-pass pada citra berwarna
def low_pass_filter_color(image):
    filtered_image = np.zeros_like(image)
    for i in range(1, image.shape[0] - 1):
        for j in range(1, image.shape[1] - 1):
            for c in range(3):
                filtered_image[i, j, c] = np.mean(image[i-1:i+2, j-1:j+2, c])  # Mengambil 3x3 area per saluran warna
    return filtered_image

# Fungsi untuk normalisasi citra ke uint8 (rentang [0, 255])
def normalize_to_uint8(image):
    return np.uint8((image / image.max()) * 255)  # Normalisasi citra ke rentang 0-255 dan konversi ke uint8

# Mengonversi citra menjadi grayscale
image_grey = convert_to_grey(my_image)

# Terapkan filter low-pass
image_gray_lowpass = low_pass_filter_grayscale(image_grey)
image_lowpass = low_pass_filter_color(my_image)

# Membuat filter high-pass dengan mengurangkan citra asli dengan hasil low-pass filter
image_gray_highpass = image_grey - image_gray_lowpass
image_highpass = my_image - image_lowpass

# Normalisasi citra ke uint8 untuk penyimpanan dan tampilan
image_grey_uint8 = normalize_to_uint8(image_grey)
image_gray_highpass_uint8 = normalize_to_uint8(image_gray_highpass)
image_highpass_uint8 = normalize_to_uint8(image_highpass)

# Menyimpan citra hasil
image.imwrite("D:\\Ikram\\Kuliah\\Semester 5\\Pengolahan Citra Digital\\PCD5\\Picture\\view_Grayscale.jpg", image_grey_uint8)
image.imwrite("D:\\Ikram\\Kuliah\\Semester 5\\Pengolahan Citra Digital\\PCD5\\Picture\\view_highpass_color.jpg", image_highpass_uint8)
image.imwrite("D:\\Ikram\\Kuliah\\Semester 5\\Pengolahan Citra Digital\\PCD5\\Picture\\view_highpass_gray.jpg", image_gray_highpass_uint8)

# Menghitung histogram untuk masing-masing citra
my_image_hist, bins = np.histogram(my_image.flatten(), bins=256, range=[0, 256])
image_gray_hist, bins = np.histogram(image_grey_uint8.flatten(), bins=256, range=[0, 256])
image_highpass_hist, bins = np.histogram(image_highpass_uint8.flatten(), bins=256, range=[0, 256])
image_gray_highpass_hist, bins = np.histogram(image_gray_highpass_uint8.flatten(), bins=256, range=[0, 256])

# Menampilkan citra asli dan hasil filter
plt.figure(figsize=(10, 10))

# Citra asli
plt.subplot(4, 2, 1)
plt.title('Citra Asli')
plt.imshow(my_image)
plt.axis('off')

plt.subplot(4, 2, 3)
plt.plot(my_image_hist, color="black")
plt.title("Histogram Citra Asli")
plt.xlabel("Intensitas")
plt.ylabel("Jumlah Piksel")

# Citra setelah high-pass filter (Berwarna)
plt.subplot(4, 2, 5)
plt.title('Citra setelah High-Pass Filter (Berwarna)')
plt.imshow(image_highpass_uint8)
plt.axis('off')

plt.subplot(4, 2, 7)
plt.plot(image_highpass_hist, color="blue")
plt.title("Histogram Citra High-Pass Filter (Berwarna)")
plt.xlabel("Intensitas")
plt.ylabel("Jumlah Piksel")

# Citra grayscale
plt.subplot(4, 2, 2)
plt.title('Citra Grayscale')
plt.imshow(image_grey_uint8, cmap='gray')
plt.axis('off')

plt.subplot(4, 2, 4)
plt.plot(image_gray_hist, color="red")
plt.title("Histogram Citra Grayscale")
plt.xlabel("Intensitas")
plt.ylabel("Jumlah Piksel")

# Citra grayscale setelah high-pass filter
plt.subplot(4, 2, 6)
plt.title('Citra Grayscale setelah High-Pass Filter')
plt.imshow(image_gray_highpass_uint8, cmap='gray')
plt.axis('off')

plt.subplot(4, 2, 8)
plt.plot(image_gray_highpass_hist, color="green")
plt.title("Histogram Citra Grayscale High-Pass Filter")
plt.xlabel("Intensitas")
plt.ylabel("Jumlah Piksel")

# Menyesuaikan layout agar tidak tumpang tindih
plt.tight_layout(pad=2.5)

plt.show()

print("Proses selesai.")
