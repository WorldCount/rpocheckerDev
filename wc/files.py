#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Работа с дубликатами
"""

__date__ = "01.03.2013"
__author__ = 'WorldCount'
__email__ = "world.count@yandex.ru"
__copyright__ = "Copyright 2013, Scr1pt1k.Ru"

import os
import hashlib
import error


def get_hash(root):
    """"Возвращает хеш файла. Если файл не найден, возбуждает исключение типа FileNotFound"""
    # Объект хеша
    file_hash = hashlib.md5()
    
    # Если файл существует,
    if os.path.exists(root):
        # открываем, 
        with open(root, u'rb') as myfile:
            
            # считываем его по-байтово,
            while True:
                content = myfile.read(1024)
                if content == '':
                    break
                # и добавляем информацию в хеш.
                file_hash.update(content)
        # Возвращаем полученный хеш в 16-ом виде.
        return file_hash.hexdigest()
    # Если файла не существует
    else:
        raise error.FileNotFound()
                
    
def isdup(one_root, two_root):
    """Возвращает является ли файл дубликатом"""
    
    # Получаем хеш файлов
    try:
        one_hash = get_hash(one_root)
    except error.FileNotFound:
        return u"Ошибка, файл '" + one_root + u"' не найден!"
    try:
        two_hash = get_hash(two_root)
    except error.FileNotFound:
        return u"Ошибка, файл '" + two_root + u"' не найден!"

    # Проверяем на дубликат
    if one_hash == two_hash:
        return True
    else:
        return False