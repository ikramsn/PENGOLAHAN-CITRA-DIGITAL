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

# Mengonversi citra menjadi grayscale
image_grey = convert_to_grey(my_image)

# Fungsi untuk menerapkan filter low-pass pada citra grayscale
def low_pass_filter_grayscale(image):
    # Membuat salinan citra untuk hasil filter
    filtered_image = np.zeros_like(image)
    
    # Mengaplikasikan filter rata-rata 3x3 pada citra grayscale
    for i in range(1, image.shape[0] - 1):  # Iterasi untuk setiap piksel (menghindari batas citra)
        for j in range(1, image.shape[1] - 1):
            # Mengambil 3x3 area dan menghitung rata-rata
            filtered_image[i, j] = np.mean(image[i-1:i+2, j-1:j+2])
    
    return filtered_image

# Fungsi untuk menerapkan filter low-pass pada citra berwarna
def low_pass_filter_color(image):
    # Membuat salinan citra untuk hasil filter
    filtered_image = np.zeros_like(image)
    
    # Mengaplikasikan filter rata-rata 3x3 pada setiap saluran warna
    for i in range(1, image.shape[0] - 1):
        for j in range(1, image.shape[1] - 1):
            for c in range(3):
                filtered_image[i, j, c] = np.mean(image[i-1:i+2, j-1:j+2, c])
    
    return filtered_image

# Terapkan filter
image_gray_lowpass = low_pass_filter_grayscale(image_grey)
image_lowpass = low_pass_filter_color(my_image)

# Konversi citra grayscale ke uint8 untuk penyimpanan
image_grey_uint8 = (image_grey / image_grey.max() * 255).astype(np.uint8)
image_gray_lowpass_uint8 = (image_gray_lowpass / image_gray_lowpass.max() * 255).astype(np.uint8)

# Menghitung histogram untuk masing-masing citra
my_image_hist, bins = np.histogram(my_image.flatten(), bins=256, range=[0, 256])
image_gray_hist, bins = np.histogram(image_grey_uint8.flatten(), bins=256, range=[0, 256])
image_lowpass_hist, bins = np.histogram(image_lowpass.flatten(), bins=256, range=[0, 256])
image_gray_lowpass_hist, bins = np.histogram(image_gray_lowpass_uint8.flatten(), bins=256, range=[0, 256])

# Menyimpan citra hasil
image.imwrite("D:\\Ikram\\Kuliah\\Semester 5\\Pengolahan Citra Digital\\PCD5\\Picture\\view_Grayscale.jpg", image_grey_uint8)
image.imwrite("D:\\Ikram\\Kuliah\\Semester 5\\Pengolahan Citra Digital\\PCD5\\Picture\\view_lowpass_color.jpg", image_lowpass)
image.imwrite("D:\\Ikram\\Kuliah\\Semester 5\\Pengolahan Citra Digital\\PCD5\\Picture\\view_lowpass_gray.jpg", image_gray_lowpass_uint8)

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

# Citra setelah low-pass filter (Berwarna)
plt.subplot(4, 2, 5)
plt.title('Citra setelah Low-Pass Filter (Berwarna)')
plt.imshow(image_lowpass.astype(np.uint8))
plt.axis('off')

plt.subplot(4, 2, 7)
plt.plot(image_lowpass_hist, color="blue")
plt.title("Histogram Citra Low-Pass Filter (Berwarna)")
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

# Citra grayscale setelah low-pass filter
plt.subplot(4, 2, 6)
plt.title('Citra Grayscale setelah Low-Pass Filter')
plt.imshow(image_gray_lowpass_uint8, cmap='gray')
plt.axis('off')

plt.subplot(4, 2, 8)
plt.plot(image_gray_lowpass_hist, color="green")
plt.title("Histogram Citra Grayscale Low-Pass Filter")
plt.xlabel("Intensitas")
plt.ylabel("Jumlah Piksel")

# Menyesuaikan layout agar tidak tumpang tindih
plt.tight_layout(pad=2.0)

plt.show()

print("Proses selesai.")
