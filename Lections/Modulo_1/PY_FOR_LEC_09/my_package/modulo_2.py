# -*- coding: utf-8 -*-
"""
Mar  5 2020
УЧЕБНЫЙ ПРИМЕР МОДУЛЯ ПАКЕТА
МОДУЛЬ ДЛЯ ФИЛЬТРАЦИИ ИЗОБРАЖЕНИЙ

"""
import numpy as np

def func(message):
    print('MOD #2 FROM PACKAGE PRINTING :',message )


# SHARP FILTER
def sharp(image) :
    rows_num = image.shape[0] ## строк
    clms_num = image.shape[1] ## колонок

    # MASK
    mask_row = 3
    mask_clm = 3
    mask_sharp = np.zeros ( (mask_row, mask_clm), dtype = np.float32)

    # MASK Q = 2
    mask_sharp[0,0] = mask_sharp[0,2] = mask_sharp[2,0] = mask_sharp[2,2] = 0
    mask_sharp[0,1] = mask_sharp[2,1] = -0.25
    mask_sharp[1,0] = mask_sharp[1,2] = -0.25
    mask_sharp[1,1] = 2



    pixel = np.zeros(3, dtype=np.float32)
    filtr_im_ = np.zeros ( (rows_num, clms_num, 3), dtype = np.int16)
    filtr_im_sharp = np.zeros ( (rows_num, clms_num, 3), dtype = np.uint8)

    for i in  range (1, (rows_num-1), 1):
        for j in  range (1, (clms_num -1), 1):
            pixel[:] = 0
            for l in range (mask_row):
                for k in range (mask_clm):
                    pixel += mask_sharp[l,k]*np.float32(image[i-(1-k), j-(1-l), : ])

            filtr_im_ [i, j, :] = np.int16(pixel [:])
            filtr_im_sharp [i, j, :]  = np.int8(pixel [:])

    return filtr_im_sharp


if __name__ == "__main__" :
    print('MODULO 2 FROM PACKAGE')
    print('МОДУЛЬ ДЛЯ ФИЛЬТРАЦИИ')
