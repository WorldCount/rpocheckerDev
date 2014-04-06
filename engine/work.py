#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Функции для работы с файлами
"""

__date__ = "25.03.14"
__author__ = 'WorldCount'
__email__ = "world.count@yandex.ru"
__copyright__ = "Copyright 2014, Scr1pt1k.Ru"

import os

def find_files(dir_files):
    """Возвращает список с файлами на обработку"""
    out_files = []
    for root, dirs, files in os.walk(dir_files):
        out_files += [os.path.join(root, name) for name in files if name[-1] == "F"]
    return out_files
