# -*- coding: utf-8 -*-
"""
Mar  5 2020
УЧЕБНЫЙ ПРИМЕР МОДУЛЯ ПАКЕТА
МОДУЛЬ ДЛЯ РАБОТЫ С ИЗОБРАЖЕНИЯМИ

"""

import numpy as np

def func(message):
    print('MOD #1 FROM PACKAGE PRINTING :',message )


def gray_im(image : "image_for_procerssing") -> "return_GRAY_image" :
   rows_num = image.shape[0] ## строк
   clms_num = image.shape[1] ## колонок
   image_out = np.zeros ( (rows_num , clms_num,3), dtype=np.uint8)
   for i in  range (rows_num):
       for j in  range (clms_num):
       # Gray image
            image_out [i, j, :] = 0.299*image[i, j, 0]+0.587*image [i, j, 1]+0.114*image [ i, j, 2]
   return image_out




if __name__ == "__main__" :
    print('MODULO 1 FROM PACKAGE')
    print('МОДУЛЬ ДЛЯ ПРЕОБРАЗОВАНИЯ ИЗОБРАЖЕНИЙ')
