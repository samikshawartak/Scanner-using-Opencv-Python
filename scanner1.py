import cv2
import numpy as np
import mapper
from tkinter import *
from tkinter.filedialog import *

root=Tk()
root.withdraw()
root.fileName=askopenfilename(filetypes=( ("Image","*.jpg"),("All files","*.*") ))

im=cv2.imread(root.fileName)
im=cv2.resize(im,(700,900))
     
r = cv2.selectROI(im)

imCrop = im[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]

imCrop=cv2.resize(imCrop,(600,800))
cv2.imshow("Image", imCrop)
cv2.imwrite("Scanned.jpg", imCrop)
cv2.waitKey(0)
