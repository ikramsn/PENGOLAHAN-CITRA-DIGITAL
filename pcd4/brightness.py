import imageio.v3 as img
import numpy as np
import matplotlib.pyplot as plt 

def blend (image1,op1,image2,op2):
    img1 = image1.astype(np.float32)
    img2 = image2.astype(np.float32)
    imgBlend = (img1 * op1) + (img2 * op2)
    imgBlend = np.clip(imgBlend,0,255)
    return imgBlend.astype(np.uint8)

img1 = img.imread("C:\\pcd4\\picture\\cat.jpg")
img2 = img.imread ("C:\\pcd4\\picture\\deer.jpeg")

imgBlend = blend(img1,0.5,img2,0.5)

img1Hist, bins = np.histogram(img1.flatten(), bins=256, range=[0, 256])
img2Hist, bins = np.histogram(img2.flatten(), bins=256, range=[0, 256])
imgBlendHist, bins = np.histogram(imgBlend.flatten(), bins=256, range=[0, 256])

for intensitas, totalPixel in enumerate(imgBlendHist):
    print(f"Intensitas: {intensitas}, Total Pixel: {totalPixel}")

plt.figure(figsize=(10,10))
plt.subplot(3,2,1)
plt.imshow(img1)

plt.subplot(3,2,2)
plt.plot(img1Hist, color= "blue" )

plt.subplot(3,2,3)
plt.imshow(img2)

plt.subplot(3,2,4)
plt.plot(img2Hist, color = "red")

plt.subplot(3,2,5)
plt.imshow(imgBlend)

plt.subplot(3,2,6)
plt.plot(imgBlendHist, color = "black")

plt.tight_layout()
plt.show()

