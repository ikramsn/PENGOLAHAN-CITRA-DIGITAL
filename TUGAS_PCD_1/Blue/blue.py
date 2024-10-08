import imageio.v3 as image
import numpy as np 

path_1 = "D:\\ikam\\TUGAS_PCD_1\\Blue\\Pict_Blue\\Kenikir.jpeg"
path_2 = "D:\\ikam\\TUGAS_PCD_1\\Blue\\Pict_Blue\\DaunSingkong.jpg"
path_3 = "D:\\ikam\\TUGAS_PCD_1\\Blue\\Pict_Blue\\DaunPepaya.jpg"

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

kenikir_blue = my_image1[:,:,2]
image_blue1 = np.zeros_like(my_image1)
image_blue1  [:,:,2] = kenikir_blue

DaunSingkong_blue = my_image2[:,:,2]
image_blue2 = np.zeros_like(my_image2)
image_blue2  [:,:,2] = DaunSingkong_blue

DaunPepaya_blue = my_image3[:,:,2]
image_blue3 = np.zeros_like(my_image3)
image_blue3  [:,:,2] = DaunPepaya_blue

image.imwrite("D:\\ikam\\TUGAS_PCD_1\\Blue\\Pict_Blue\\Kenikir_blue.jpeg", image_blue1)
image.imwrite("D:\\ikam\\TUGAS_PCD_1\\Blue\\Pict_Blue\\DaunSingkong_blue.jpg", image_blue2)
image.imwrite("D:\\ikam\\TUGAS_PCD_1\\Blue\\Pict_Blue\\DaunPepaya_blue.jpg", image_blue3)

print(f"Dimensi gambar adalah {my_image1.shape}")
print(f"Dimensi gambar adalah {my_image2.shape}")
print(f"Dimensi gambar adalah {my_image3.shape}")

print("proses selesai")