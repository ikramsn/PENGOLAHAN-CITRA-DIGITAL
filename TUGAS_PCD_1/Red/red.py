import imageio.v3 as image
import numpy as np 

path_1 = "D:\\ikam\\TUGAS_PCD_1\\Red\\Pict_Red\\Kenikir.jpeg"
path_2 = "D:\\ikam\\TUGAS_PCD_1\\Red\\Pict_Red\\DaunSingkong.jpg"
path_3 = "D:\\ikam\\TUGAS_PCD_1\\Red\\Pict_Red\\DaunPepaya.jpg"

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

kenikir_red = my_image1[:,:,0]
image_red1 = np.zeros_like(my_image1)
image_red1  [:,:,0] = kenikir_red

DaunSingkong_red = my_image2[:,:,0]
image_red2 = np.zeros_like(my_image2)
image_red2  [:,:,0] = DaunSingkong_red

DaunPepaya_red = my_image3[:,:,0]
image_red3 = np.zeros_like(my_image3)
image_red3  [:,:,0] = DaunPepaya_red

image.imwrite("D:\\ikam\\TUGAS_PCD_1\\Red\\Pict_Red\\Kenikir_red.jpeg", image_red1)
image.imwrite("D:\\ikam\\TUGAS_PCD_1\\Red\\Pict_Red\\DaunSingkong_red.jpg", image_red2)
image.imwrite("D:\\ikam\\TUGAS_PCD_1\\Red\\Pict_Red\\DaunPepaya_red.jpg", image_red3)

print(f"Dimensi gambar adalah {my_image1.shape}")
print(f"Dimensi gambar adalah {my_image2.shape}")
print(f"Dimensi gambar adalah {my_image3.shape}")
print("proses selesai")

