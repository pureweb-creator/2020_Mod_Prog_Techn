# -*- coding: utf-8 -*-
"""
****** QT5 ******
Installation
conda install -c dsdale24 qt5

Created on Wed Apr  1 17:37:34 2020

@author: E.Bashkov

Qt for Python Documentation
https://doc.qt.io/qtforpython/contents.html

"""
import sys
# import qtpy
# from qtpy import QtGui, QtWidgets, QtCore
from PyQt5 import QtWidgets, uic


app = QtWidgets.QApplication(sys.argv)
win = uic.loadUi("Simple_Test_01.ui") # расположение файла .ui

win.show()



# app.exec_()           #  Запускаем бесконечный цикл обработки app
                        # !! НЕ ЗАКРЫВАЕТ ЯДРО КОНСОЛИ  ИНТЕРПРЕТАТОРА
#sys.exit(app.exec_())  #  Запускаем бесконечный цикл обработки app
                        # !! НЕ ЗАКРЫВАЕТ ЯДРО КОНСОЛИ  ИНТЕРПРЕТАТОРА

sys.exit()    # ВЫХОДИТ СРАЗУ  -- ОКНО РАБОТАЕТ
