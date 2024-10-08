import imageio.v3 as image
import numpy as np 

path_1 = "D:\\ikam\\TUGAS_PCD_1\\Treshold\\Pict_BW\\Kenikir.jpeg"
path_2 = "D:\\ikam\\TUGAS_PCD_1\\Treshold\\Pict_BW\\DaunSingkong.jpg"
path_3 = "D:\\ikam\\TUGAS_PCD_1\\Treshold\\Pict_BW\\DaunPepaya.jpg"

my_image1 = image.imread(path_1)
my_image2 = image.imread(path_2)
my_image3 = image.imread(path_3)

def process_to_bw(image):
    if len(image.shape) < 3:
        print("Gambar harus RGB")
        exit()

    red = image[:, :, 0]
    green = image[:, :, 1]
    blue = image[:, :, 2]
    grey = 0.2989 * red + 0.5870 * green + 0.1140 * blue 

    threshold = 100
    bw_image = np.where(grey > threshold, 255, 0).astype(np.uint8) 

    bw_image_rgb = np.stack([bw_image]*3, axis=-1)
    
    return bw_image_rgb

bw_image1 = process_to_bw(my_image1)
bw_image2 = process_to_bw(my_image2)
bw_image3 = process_to_bw(my_image3)

image.imwrite("D:\\ikam\\TUGAS_PCD_1\\Treshold\\Pict_BW\\Kenikir_BW.jpeg", bw_image1)
image.imwrite("D:\\ikam\\TUGAS_PCD_1\\Treshold\\Pict_BW\\DaunSingkong_BW.jpg", bw_image2)
image.imwrite("D:\\ikam\\TUGAS_PCD_1\\Treshold\\Pict_BW\\DaunPepaya_BW.jpg", bw_image3)

print("Proses selesai.")
