import PIL
import cv2
import numpy as np
import random

WIDTH = HEIGHT = 1000

blank_grayscale_img = np.zeros((WIDTH, HEIGHT, 1), dtype=np.uint8)

background_grayscale_black = blank_grayscale_img[:, :, :]
cv2.imwrite("background_grayscale_black.png", background_grayscale_black)

background_grayscale_white = blank_grayscale_img[:, :, :]
for i in range(HEIGHT):
    for j in range(WIDTH):
        background_grayscale_white[i, j] = 255
cv2.imwrite("background_grayscale_white.png", background_grayscale_white)

background_grayscale_noise_random = blank_grayscale_img[:, :, :]
for i in range(HEIGHT):
    for j in range(WIDTH):
        background_grayscale_noise_random[i, j] = random.randint(0, 255)
cv2.imwrite("background_grayscale_noise_random.png",
            background_grayscale_noise_random)

blank_8_bit_color_img = np.zeros((WIDTH, HEIGHT, 3), dtype=np.uint8)

background_8_bit_color_black = blank_8_bit_color_img[:, :, :]
cv2.imwrite("background_8_bit_color_black.png", background_8_bit_color_black)

background_8_bit_color_white = blank_8_bit_color_img[:, :, :]
for i in range(HEIGHT):
    for j in range(WIDTH):
        for k in range(3):
            background_8_bit_color_white[i, j, k] = 255
cv2.imwrite("background_8_bit_color_white.png", background_8_bit_color_white)

background_8_bit_color_noise_random = blank_8_bit_color_img[:, :, :]
for i in range(HEIGHT):
    for j in range(WIDTH):
        for k in range(3):
            background_8_bit_color_noise_random[i, j, k] = (random.randint(0, 255))
cv2.imwrite("background_8_bit_color_noise_random.png",
            background_8_bit_color_noise_random)
