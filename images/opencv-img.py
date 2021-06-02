import cv2
import matplotlib.pyplot as plt

image= cv2.imread('img.png')

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)) # fix bgr coloring of opencv
plt.gca().axis("off")
plt.show()

