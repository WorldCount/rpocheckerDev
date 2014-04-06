#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Классы ошибок
"""

__date__ = "01.03.2013"
__author__ = 'WorldCount'
__email__ = "world.count@yandex.ru"
__copyright__ = "Copyright 2013, Scr1pt1k.Ru"


class NotFound(Exception):

    """
    Общий класс для ошибок
    @author WorldCount
    @version 0.1
    @date 2014/03/25
    """

    pass


class FileNotFound(NotFound):

    """
    Файл не найден
    @author WorldCount
    @version 0.1
    @date 2014/03/25
    """

    pass


class SectionNotFound(NotFound):

    """
    Секция в конфиге не найдена
    @author WorldCount
    @version 0.1
    @date 2014/03/25
    """

    pass