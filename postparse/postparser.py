#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Парсер почтового файла
"""

__date__ = "25.03.14"
__author__ = 'WorldCount'
__email__ = "world.count@yandex.ru"
__copyright__ = "Copyright 2014, Scr1pt1k.Ru"

from postparse import postfile, packfile, parsererror


class PostParser(object):

    """
    Парсит почтовый файл.
    @author WorldCount
    @version 0.1
    @date 2014/03/25
    """

    def __init__(self, link):

        self.link = link
        self.pack = self.ispack()
        self.first_string = ["OPERTYPE", "OPERDATE", "BARCODE", "INDEXTO", "MAILDIRECT", "TRANSTYPE", "MAILTYPE",
                            "MAILCTG", "MAILRANK", "SENDCTG", "POSTMARK", "MASS", "PAYMENT", "VALUE", "PAYTYPE",
                            "MASSRATE", "INSRRATE", "AIRRATE", "ADVALTAX", "SALETAX", "RATE", "OPERATTR", "INDEXOPER",
                            "INDEXNEXT", "COMMENT"]
        self.work_object = ""

    def ispack(self):
        """Проверяет, является ли файл архивом"""
        with open(self.link) as f:
            line = f.readline()
        symbol = line[0:2].lower()
        if symbol == "op":
            return False
        if symbol == "pk":
            return True
        else:
            return None

    def load(self):
        """Загружает файл рпо"""
        if self.pack is True:
            myobject = packfile.PostPackFile(self.link)
            myobject.set_pack(True)
        elif self.pack is False:
            myobject = postfile.PostFile(self.link)
            myobject.set_pack(False)
        else:
            raise parsererror.TypeFileError(self.link)

        # Оставляем данные объекта себе для работы над ним
        self.work_object = myobject
        return myobject