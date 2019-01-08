#import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

from tensorflow import  keras
mnist = keras.datasets.mnist
(train_images, train_labels),(test_images, tet_labels) = mnist.load_data()

print("훈련 이미지 :", train_images.shape)
print("훈련 라벨 :", train_labels.shape)
print("테스트 이미지 :", train_images.shape)
print("테스트 라벨 :", train_labels.shape)

mnist_idx = 100

print('[label]')
print('number label = ', train_labels[mnist_idx])
print('\n')

print('[image]')

for row in train_images[mnist_idx]:
    for col in row:
        print("%10f" % col, end="")
    print('\n')
print('\n')

plt.figure(figsize=(5, 5))
image = train_images[mnist_idx]
plt.imshow(image)
plt.show()
