#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Ошибки парсера почтовых файлов
"""

__date__ = "25.03.14"
__author__ = 'WorldCount'
__email__ = "world.count@yandex.ru"
__copyright__ = "Copyright 2014, Scr1pt1k.Ru"


class PostError(Exception):

    """
    Общий класс для ошибок почтовых файлов
    @author WorldCount
    @version 0.1
    @date 2014/03/25
    """

    pass


# ОШИБКИ ФАЙЛА
class PostFileError(PostError):

    """
    Ошибка при работе с почтовым файлом
    @author WorldCount
    @version 0.1
    @date 2014/03/25
    """

    def __init__(self, link_file):
        self.link_file = link_file


class FileInZipNotFound(PostFileError):

    """
    Не найден файл в архиве
    @author WorldCount
    @version 0.1
    @date 2014/03/25
    """

    pass


class TypeFileError(PostFileError):

    """
    Ошибка типа почтового файла
    @author WorldCount
    @version 0.1
    @date 2014/03/25
    """

    pass


# ОШИБКИ ПАРСИНГА
class PostParseError(PostError):

    """
    Ошибка парсинга почтового файла
    @author WorldCount
    @version 0.1
    @date 2014/03/25
    """

    def __init__(self, line, link_file):
        self.line = line
        self.link_file = link_file


class ParseNameError(PostParseError):

    """
    Ошибка парсинга имени почтового файла
    @author WorldCount
    @version 0.1
    @date 2014/03/25
    """

    pass


class ParseStringError(PostParseError):

    """
    Ошибка парсинга строки почтового файла
    @author WorldCount
    @version 0.1
    @date 2014/03/25
    """

    pass