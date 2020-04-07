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
from PyQt5 import QtWidgets, uic
# ИЗ НАШЕГО МОДУЛЯ () ИМПОРТИРУЕМ КЛАСС Главного окна
from Simple_Test_01 import Ui_MainWindow

class Test_1_win(QtWidgets.QMainWindow):
    def __init__(self):
        # явный вызов конструктора родительского класса
        super(Test_1_win, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


app = QtWidgets.QApplication(sys.argv) # Создаем объект - приложение
appl = Test_1_win() # Создаем экземпляр  нашего окна (от подкласса QtWidgets.QMainWindow)

appl.show() # Выводим


# app.exec_()           #  Запускаем бесконечный цикл обработки app
                        # !! НЕ ЗАКРЫВАЕТ ЯДРО КОНСОЛИ  ИНТЕРПРЕТАТОРА
#sys.exit(app.exec_())  #  Запускаем бесконечный цикл обработки app
                        # !! НЕ ЗАКРЫВАЕТ ЯДРО КОНСОЛИ  ИНТЕРПРЕТАТОРА

sys.exit()    # ВЫХОДИТ СРАЗУ  -- ОКНО РАБОТАЕТ
