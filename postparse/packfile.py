#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Запакованный почтовый файл
"""

__date__ = "25.03.14"
__author__ = 'WorldCount'
__email__ = "world.count@yandex.ru"
__copyright__ = "Copyright 2014, Scr1pt1k.Ru"

from postparse import postfile, parsererror
from zipfile import ZipFile


class PostPackFile(postfile.PostFile):

    """
    Запакованный почтовый файл
    @author WorldCount
    @version 0.1
    @date 2014/03/25
    """

    def __init__(self, link):
        postfile.PostFile.__init__(self, link)

    def get_all_mail(self):
        """Получает список отправлений"""
        with ZipFile(self.link) as myzip:
            # Открываем архив, находим файл и передаем его дескриптор
            try:
                f = myzip.namelist()[0]
                return self._parse_mail(myzip.open(f))
            except IndexError:
                raise parsererror.FileInZipNotFound(self.name)