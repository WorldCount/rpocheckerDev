#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Разные утилиты для работы
"""

__date__ = "17.11.2012"
__author__ = 'WorldCount'
__email__ = "world.count@yandex.ru"
__copyright__ = "Copyright 2012, Scr1pt1k.Ru"


import datetime
import os.path


def get_current_date():
    """Получает текущую дату"""
    currentdate = datetime.datetime.now()
    return currentdate.strftime("%d.%m.%y %H:%M")


def set_slash(string):
    """Добавляет слеш в конец пути, если его нет"""
    num = len(string)
    if string[num-1:num] != "\\":
        string += "\\"
    return string


def get_script_dir():
    """Получает каталог скрипта"""
    string = os.path.abspath(os.curdir)
    string = set_slash(string)
    return string


def get_file_date(file_root):
    """Получает дату изменения файла"""
    if os.path.exists(file_root):
        stamp = os.path.getmtime(file_root)
        dfile = datetime.datetime.fromtimestamp(stamp)
        return dfile.strftime("%d.%m.%y %H:%M")
    else:
        return False
    

def fromat_date_time(stamp):
    """"""
    temp = datetime.datetime.fromtimestamp(stamp)
    return temp.strftime("%d.%m.%y"), temp.strftime("%H:%M:%S")