import imageio.v3 as image
import numpy as np 

path_1 = "D:\\ikam\\TUGAS_PCD_1\\Green\\Pict_Green\\Kenikir.jpeg"
path_2 = "D:\\ikam\\TUGAS_PCD_1\\Green\\Pict_Green\\DaunSingkong.jpg"
path_3 = "D:\\ikam\\TUGAS_PCD_1\\Green\\Pict_Green\\DaunPepaya.jpg"

my_image1 = image.imread(path_1)
my_image2 = image.imread(path_2)
my_image3 = image.imread(path_3)

print(my_image1.shape[0])
if (len(my_image1.shape)<3):
    print("Gambar Harus RGB")
    exit()

print(my_image2.shape[0])
if (len(my_image2.shape)<3):
    print("Gambar Harus RGB")
    exit()

print(my_image3.shape[0])
if (len(my_image3.shape)<3):
    print("Gambar Harus RGB")
    exit()

kenikir_green = my_image1[:,:,1]
image_green1 = np.zeros_like(my_image1)
image_green1  [:,:,1] = kenikir_green

DaunSingkong_green = my_image2[:,:,1]
image_green2 = np.zeros_like(my_image2)
image_green2  [:,:,1] = DaunSingkong_green

DaunPepaya_green = my_image3[:,:,1]
image_green3 = np.zeros_like(my_image3)
image_green3  [:,:,1] = DaunPepaya_green

image.imwrite("D:\\ikam\\TUGAS_PCD_1\\Green\\Pict_Green\\Kenikir_green.jpeg", image_green1)
image.imwrite("D:\\ikam\\TUGAS_PCD_1\\Green\\Pict_Green\\DaunSingkong_green.jpg", image_green2)
image.imwrite("D:\\ikam\\TUGAS_PCD_1\\Green\\Pict_Green\\DaunPepaya_green.jpg", image_green3)

print(f"Dimensi gambar adalah {my_image1.shape}")
print(f"Dimensi gambar adalah {my_image2.shape}")
print(f"Dimensi gambar adalah {my_image3.shape}")
print("proses selesai")