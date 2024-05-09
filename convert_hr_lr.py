import cv2
import os

images = 'data/images/'
hr_path = 'data/hr_images/'
lr_path = 'data/lr_images/'

for i,img in enumerate(os.listdir(images)):
    image = cv2.imread(images + img)
    hr_img = cv2.resize(image, (256, 256))
    cv2.imwrite(hr_path + img, hr_img)
    lr_img = cv2.resize(image, (64, 64))
    cv2.imwrite(lr_path + img, lr_img)