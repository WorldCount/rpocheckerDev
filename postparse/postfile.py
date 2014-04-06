#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Незапакованный почтовый файл
"""

__date__ = "25.03.14"
__author__ = 'WorldCount'
__email__ = "world.count@yandex.ru"
__copyright__ = "Copyright 2014, Scr1pt1k.Ru"

import re
import os.path
import hashlib
from postparse import parsererror


class PostFile(object):

    """
    Незапакованный почтовый файл.
    @author WorldCount
    @version 0.1
    @date 2014/03/25
    """

    def __init__(self, link):

        # Номер базового ОПС
        self.base_ops_num = "127950"
        # Ссылка на файл
        self.link = link
        (self._dir_file, self._name_file) = os.path.split(link)
        # Имя файла
        self.name = self.get_name_file()
        # Список отправлений
        self.list_mail = self.get_all_mail()
        # Количество строк в файле
        self.sum_string = len(self.list_mail)
        # Номер отделения
        self.ops_number = self.list_mail[0][22]
        # Дубликат, значение по умолчанию
        self.double = False
        # Хеш файла
        self.hash = self._get_hash()
        # Штамп даты поступления файла
        self.date_file = self._get_date_file()
        # Версия ПО
        self.version = self._get_version_file()
        # Тип файла
        self.file_type = ""
        # Количество ошибок в файле
        self.error = 0
        # Является ли файл архивом
        self.pack = ""
        # Окно, с которого поступил файл
        self.window = self.get_window_file()

    def get_name_file(self):
        """Возвращает имя файла"""
        find_name = re.findall("[0-9]+", self._name_file)
        return_name = find_name[0] + "." + find_name[1] + "F"
        try:
            len_name = len(return_name)
        except IndexError:
            raise parsererror.ParseNameError

        if len_name == 12:
            return return_name
        if len_name == 11:
            return "1" + return_name
        else:
            raise parsererror.ParseNameError

    def get_window_file(self):
        """Возвращает номер окна файла"""
        find_name = re.findall("[0-9]{8}", self._dir_file)
        if len(find_name) == 1:
            return find_name[0]
        else:
            return None

    def get_all_mail(self):
        """Получает список отправлений"""
        with open(self.link, "r") as rpofile:
            # Открываем файл и передаем дескриптор дальше
            return self._parse_mail(rpofile)

    def _parse_mail(self, link_file):
        """Парсит отправления, возвращает список"""
        rpo_list = self._post_open(link_file)
        # Удаляем первую строку, т.к. там нет нужных данных
        del rpo_list[0]
        return rpo_list

    def _post_open(self, link_file):
        """Парсит почтовый файл, исправляет ошибки, возвращает список"""
        my_list = []
        for num, line in enumerate(link_file):
            temp_line = line.rstrip().split("|")
            if len(temp_line) == 25:
                my_list.append(temp_line)
            else:
                raise parsererror.ParseStringError(num, self.name)
        return my_list

    def set_double(self, value):
        """Устанавливает значение дубликата"""
        if type(value) is bool:
            self.double = value
        else:
            return False

    def set_pack(self, value):
        """Устанавливает свойство является ли файл архивом"""
        if type(value) is bool:
            self.pack = value
            return True
        else:
            return False

    def _get_hash(self):
        """Возвращает MD5-хеш файла"""
        file_hash = hashlib.md5()
        mdsum = ""
        # Складываем номера отправлений в одну строку
        for rpo in self.list_mail:
            mdsum += rpo[2]
        file_hash.update(mdsum)
        return file_hash.hexdigest()

    def _get_date_file(self):
        """Возвращает штамп даты и времени файла"""
        stamp = os.path.getmtime(self.link)
        return stamp

    def _get_version_file(self):
        """Возвращает версию ПО файла"""
        if self.name[0:6] == self.base_ops_num: return "Base"
        patern = "([PDWRN]{1,2}_*[0-9]\.*[0-9]*\.*[0-9]*\.*[0-9])"
        mycompile = re.compile(patern)
        list_version = []

        for num, row in enumerate(self.list_mail):
            try:
                tmp = mycompile.search(row[24])
            except IndexError:
                raise parsererror.ParseStringError(num, self.name)
            if tmp is None:
                continue
            if tmp.group() in list_version:
                continue
            else:
                list_version.append(tmp.group())

        if len(list_version) > 1:
            return "Base"
        else:
            return list_version[0]