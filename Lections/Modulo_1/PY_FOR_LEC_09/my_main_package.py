
# -*- coding: utf-8 -*-
"""
ПРИМЕР РАБОТЫ С ПАКЕТОМ РАБОТЫ С ИЗОБРАЖЕНИЯМИ


"""


import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
plt.rcParams['font.size'] = 18

import my_package
print(my_package.discript)

import my_package.modulo_1 as m1
import my_package.modulo_2 as m2

filename = 'Lenna.png'
test_im = io.imread(filename)
plt.title('ИСХОДНОЕ')
plt.imshow(test_im)
plt.show()

gray_image = m1.gray_im(test_im)

plt.title('ПОЛУТОН')
plt.imshow(gray_image)
plt.show()


sharp_image = m2.sharp(gray_image)

plt.title('РЕЗКОСТЬ')
plt.imshow(sharp_image)
plt.show()

