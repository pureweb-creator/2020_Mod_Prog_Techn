# -*- coding: utf-8 -*-
"""
****** QT5 ******
Installation
conda install -c dsdale24 qt5

Created on Wed 05 aprl 2020

@author: E.Bashkov

Qt for Python Documentation
https://doc.qt.io/qtforpython/contents.html


Data Visualization Tool Tutorial
https://doc.qt.io/qtforpython/tutorials/datavisualize/index.html

"""

import sys  # Для передачи аргументов
import os  # Для отображения содержимого папки
import pandas as pd
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt, QAbstractTableModel, QModelIndex
from PyQt5.QtGui import QColor


class MainWindow(QtWidgets.QMainWindow):
    '''
    ИНИЦИАЛИЗАЦИЯ ОСНОВНОГО ОКНА ПРИЛОЖЕНИЯ

    '''
    def __init__(self, widget):

        QtWidgets.QMainWindow.__init__(self)
        self.setWindowTitle("FLORIDA info")
        self.setCentralWidget(widget)

        # Menu
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")

        # Exit QAction
        exit_action = QtWidgets.QAction("Exit", self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.triggered.connect(self.close)

        self.file_menu.addAction(exit_action)

        # Status Bar
        self.status = self.statusBar()
        self.status.showMessage("Loaded DATA")


# СОЗДАЕМ КЛАСС ТАБЛИЦІ ОТОБРАЖЕНИЯ
class CustomTableModel(QAbstractTableModel):
    '''
    КЛАСС СОЗДАНИЯ ТАБЛИЦЫ ОТОБРАЖЕНИЯ

    '''
    def __init__(self, data=None):
        QAbstractTableModel.__init__(self)
        self.load_data(data)

    def load_data(self, data):
        '''
        ВЫБИРАЕМ ЧТО БУДЕМ ГРУЗИТЬ В ТАБЛИЦУ
        Например: ДВЕ КОЛОНИКИ с ЗАДАННЫМИ ИМЕНАМИ
        И ОПРЕДЕЛЯЕМ ЧИСЛО КОЛОНОК И ЧИСЛО СТРОК
        '''
        self.inpt_pID = data['policyID'].values
        self.inpt_fl = data['fl_site_limit'].values

        self.column_count = 2
        self.row_count = len(self.inpt_pID)

    def rowCount(self, parent=QModelIndex()):
        return self.row_count

    def columnCount(self, parent=QModelIndex()):
        return self.column_count

    def headerData(self, section, orientation, role):
        '''
        ЗАДАЕМ ВИДИМЫЕ ИМЕНА КОЛОНОК
        '''
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            return ("Номер полиса", "Лимит")[section]
        else:
            return "{}".format(section)

    def data(self, index, role=Qt.DisplayRole):
        '''
        ЗАГРУЖАЕМ ДАННЫЕ В ТАБЛИЦУ
        '''
        column = index.column()
        row = index.row()

        if role == Qt.DisplayRole:
            if column == 0:
                raw_date = self.inpt_pID[row]

                date = "{}".format(self.inpt_pID[row])
                return date[:]
            elif column == 1:
                return "{}".format(self.inpt_fl[row])
        elif role == Qt.BackgroundRole:
            return QColor(Qt.white)
        elif role == Qt.TextAlignmentRole:
            return Qt.AlignRight

        return None


class Widget(QtWidgets.QWidget):
    '''
     ИНИЦИАЛИЗАЦИЯ ВИДЖЕТА ОТОБРАЖЕНИЯ ТАБЛИЦЫ
    '''
    def __init__(self, data):
        QtWidgets.QWidget.__init__(self)

        # Getting the Model
        self.model = CustomTableModel(data)

        # Creating a QTableView
        self.table_view = QtWidgets.QTableView()
        self.table_view.setModel(self.model)

        # QTableView Headers
        self.horizontal_header = self.table_view.horizontalHeader()
        self.vertical_header = self.table_view.verticalHeader()
        self.horizontal_header.setSectionResizeMode(
                                QtWidgets.QHeaderView.ResizeToContents
                                )
        self.vertical_header.setSectionResizeMode(
                              QtWidgets.QHeaderView.ResizeToContents
                              )
        self.horizontal_header.setStretchLastSection(True)

        # QWidget Layout
        self.main_layout = QtWidgets.QHBoxLayout()
        size = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)

        ## Left layout
        size.setHorizontalStretch(1)
        self.table_view.setSizePolicy(size)
        self.main_layout.addWidget(self.table_view)

        # Set the layout to the QWidget
        self.setLayout(self.main_layout)




if __name__ == "__main__":
    '''
    С ПОМОЩЬЮ PANDAS ЧИТАЕМ CSV ФАЙЛ (ОАЗДЕЛИТЕЛЬ ЗАПЯТАЯ)
    ЗАДАЕМ КОЛИЧЕСТВО СЧИТЫВАЕМЫХ ЗАПИСЕЙ

    '''
    data = pd.read_csv('CSV_Data/FL_insurance_sample_.csv', nrows = 100)
    # ДЛЯ ПРОВЕРКИ ВЫВОДИМ ЗАПИСИ
    print(data)

    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    widget = Widget(data)
    appl5 = MainWindow (widget)
    appl5.show()  # Показываем окно
    sys.exit()    # ВЫХОДИТ СРАЗУ  -- ОКНО РАБОТАЕТ



