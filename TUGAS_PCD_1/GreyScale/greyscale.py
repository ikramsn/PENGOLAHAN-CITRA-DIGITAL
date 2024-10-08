import imageio.v3 as image
import numpy as np 

path_1 = "D:\\ikam\\TUGAS_PCD_1\\GreyScale\\Pict_Grey\\Kenikir.jpeg"
path_2 = "D:\\ikam\\TUGAS_PCD_1\\GreyScale\\Pict_Grey\\DaunSingkong.jpg"
path_3 = "D:\\ikam\\TUGAS_PCD_1\\GreyScale\\Pict_Grey\\DaunPepaya.jpg"

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

def convert_to_grey(image):
    red = image[:, :, 0]
    green = image[:, :, 1]
    blue = image[:, :, 2]
    grey = (red + green + blue) / 3
    grey_image = np.zeros_like(image)
    grey_image[:, :, 0] = grey
    grey_image[:, :, 1] = grey
    grey_image[:, :, 2] = grey
    return grey_image

image_grey1 = convert_to_grey(my_image1)
image_grey2 = convert_to_grey(my_image2)
image_grey3 = convert_to_grey(my_image3)

image.imwrite("D:\\ikam\\TUGAS_PCD_1\\GreyScale\\Pict_Grey\\Kenikir_grey.jpeg", image_grey1)
image.imwrite("D:\\ikam\\TUGAS_PCD_1\\GreyScale\\Pict_Grey\\DaunSingkong_grey.jpg", image_grey2)
image.imwrite("D:\\ikam\\TUGAS_PCD_1\\GreyScale\\Pict_Grey\\DaunPepaya_grey.jpg", image_grey3)

print("Proses selesai.")

