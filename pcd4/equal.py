import imageio.v3 as image
import numpy as np
import matplotlib.pyplot as plt 

def equalization(image):
    hist, bins = np.histogram(image.flatten(), bins = 256, range = [0,256])
    cdf = hist.cumsum()
    cdf_normalized = (cdf/cdf.max()) * 255
    imgEqual = np.interp(image.flatten(), bins [:-1], cdf_normalized)
    return imgEqual.reshape(image.shape).astype(np.uint8)

image = image.imread("C:\\pcd4\\picture\\city.jpeg")
imageEqual = equalization(image)

hist, bins = np.histogram(image.flatten(), bins=256, range=[0, 256])
histEqual, bins = np.histogram(imageEqual.flatten(), bins=256, range=[0, 256])

plt.figure(figsize = (10,10))
plt.subplot(2,2,1)
plt.imshow(image)

plt.subplot(2,2,2)
plt.plot(hist)

plt.subplot(2,2,3)
plt.imshow(imageEqual)

plt.subplot(2,2,4)
plt.plot(histEqual)

plt.tight_layout()
plt.show()