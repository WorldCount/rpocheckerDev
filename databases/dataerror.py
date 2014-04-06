#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Ошибки при работе с БД
"""

__date__ = "29.03.14"
__author__ = 'WorldCount'
__email__ = "world.count@yandex.ru"
__copyright__ = "Copyright 2014, Scr1pt1k.Ru"


class DatabaseError(Exception):

    """
    Главный класс ошибок БД
    @author WorldCount
    @version 0.1
    @date 2014/03/29
    """

    pass


class DataFileNotFound(DatabaseError):

    """
    Файл с данными не найден
    @author WorldCount
    @version 0.1
    @date 2014/03/29
    """

    def __init__(self, name, link):
        self.name = name
        self.link = link


class ParamError(DatabaseError):

    """
    Не хватает параметров
    @author WorldCount
    @version 0.1
    @date 2014/03/29
    """

    def __init__(self, param_name, where):
        # Имя параметра
        self.param_name = param_name
        # Где не хватает
        self.where = where