# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 13:51:11 2020

@author: 210_01
"""

case_0  = False
if case_0 :
    print('***CASE 0***')
    import sys
    print(sys.path)


case_1  = True
if case_1 :
    print('***CASE 1***')
    import modulo_1
    print(dir(func))
    import modulo_2
    modulo_1.func('This is FIRST modul')
    modulo_2.func('This is SECOND modul')
    print('MODUL 1 ATTRIBUTES :', dir(modulo_1))
    print('FUNC    ATTRIBUTES :', dir(func))
    print('FUNC          NAME :', func.__name__)

case_2  = False
if case_2 :
    print('***CASE 2***')
    from modulo_1 import func
    from modulo_2 import func
    func('This is FIRST modul')
    func('This is SECOND modul')



