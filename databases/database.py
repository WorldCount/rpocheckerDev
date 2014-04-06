#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Работа с базой данных
"""

__date__ = "25.03.14"
__author__ = 'WorldCount'
__email__ = "world.count@yandex.ru"
__copyright__ = "Copyright 2014, Scr1pt1k.Ru"

import sqlite3
import os
from wc import utils
from databases import dataerror


class DataBase(object):

    """
    Общий класс для работы с БД
    @author WorldCount
    @version 0.1
    @date 2014/03/25
    """

    def __init__(self):

        # Директория скрипта
        self.script_dir = utils.get_script_dir()
        # Директория c данными и БД
        self.data_dir = self.script_dir + "data\\"
        # Имя БД
        self.base_name = "base.db"
        # Полный путь к БД
        self.base = self.data_dir + self.base_name

        # Если нету папки, то создаем
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)

    def connect(self):
        """Соединение с БД"""
        return sqlite3.connect(self.base)

    def _insert_data(self, query, data_list):
        """Вставка данных в таблицу"""
        if query is False:
            raise dataerror.ParamError("query", "_insert_data(self, query, data_list)")
        if data_list is False:
            raise dataerror.ParamError("data_list", "_insert_data(self, query, data_list)")

        with self.connect() as conn:
            curr = conn.cursor()
            curr.executemany(query, data_list)

    def _create_table(self, query):
        """Создание таблицы"""
        if query is False:
            raise dataerror.ParamError("query", "_create_table(self, query)")

        with self.connect() as conn:
            curr = conn.cursor()
            curr.execute(query)