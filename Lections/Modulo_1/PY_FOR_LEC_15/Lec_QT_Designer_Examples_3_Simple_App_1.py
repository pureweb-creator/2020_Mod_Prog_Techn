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
import sys  # Для передачи аргументов
import os  # Для отображения содержимого папки
from PyQt5 import QtWidgets, uic


# ИЗ НАШЕГО МОДУЛЯ () ИМПОРТИРУЕМ КЛАСС Главного окна
from Simple_Test_03_Simpl_App_1 import Ui_MainWindow

class Test_3_win(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.setupUi(self)
        self.pushButton_1.clicked.connect((self.browse_folder))


    def browse_folder(self):
        self.listWidget.clear()  # Удаляем если в списке есть элементы
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")
        # открыть диалог выбора директории и установить значение переменной
        # равной пути к выбранной директории

        if directory:  # не продолжать выполнение, если пользователь не выбрал директорию
            for file_name in os.listdir(directory):  # для каждого файла в директории
                self.listWidget.addItem(file_name)   # добавить файл в listWidget


app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
appl3 = Test_3_win ()  # Создаём appl3 - объект класса Test_3_win
appl3.show()  # Показываем окно
sys.exit()    # ВЫХОДИТ СРАЗУ  -- ОКНО РАБОТАЕТ

