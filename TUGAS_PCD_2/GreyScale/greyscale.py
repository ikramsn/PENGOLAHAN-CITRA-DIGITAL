import imageio.v3 as image
import numpy as np
import matplotlib.pyplot as plt 

path = "D:\\ikam\\TUGAS_PCD_2\\GreyScale\\Pict_Grey\\view.jpeg"

my_image = image.imread(path)

red = my_image[:, :, 0]
green = my_image[:, :, 1]
blue = my_image[:, :, 2]

grey = (red + green + blue) / 3

grey_image = np.zeros_like(my_image)
grey_image[:, :, 0] = grey
grey_image[:, :, 1] = grey
grey_image[:, :, 2] = grey

gs_hist, bins = np.histogram (grey_image.flatten(),bins=256,range=[0,256])
gRnormalized = gs_hist/gs_hist.sum()

for intensity, total_pixels in enumerate(gs_hist):
    print(f"Intensitas {intensity}: {total_pixels} piksel")

dominant_intensity = np.argmax(gs_hist)
max_pixels = gs_hist[dominant_intensity]
print(f"Intensitas yang dominan: {dominant_intensity} dengan {max_pixels} piksel.")

plt.figure (figsize =( 8,6))
plt.subplot(3,2,1)
plt.imshow(grey_image)
plt.title("GreySclae")

plt.subplot(3,2,2)
plt.plot(gs_hist, color = "red")
plt.title("Histogram")
plt.xlabel("Intensitas")
plt.ylabel("Jumlah Pixel")

plt.subplot(3,2,3)
plt.plot(gRnormalized, color = "blue")
plt.title("Normalisasi")
plt.xlabel("Intensitas")
plt.ylabel("Jumlah Pixel")

plt.tight_layout()
plt.show()

print("Proses selesai.")
