#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Конфиг с начальными данными
"""

__date__ = "29.03.14"
__author__ = 'WorldCount'
__email__ = "world.count@yandex.ru"
__copyright__ = "Copyright 2014, Scr1pt1k.Ru"

from databases import database
from wc import utils

class DefaultConfig(database.DataBase):

    """
    Конфиг по-умолчанию
    @author WorldCount
    @version 0.1
    @date 2014/03/29
    """

    def __init__(self):
        database.DataBase.__init__(self)

        self.table_name_config = "Config"

        # ДАННЫЕ ПО-УМОЛЧАНИЮ
        # Номер базового ОПС
        self.num_base_ops = u"127950"
        # Директория файлов на обработку
        self.dir_in_files = u"C:\IN\\"
        # Директория файлов на отправку
        self.dir_out_files = u"C:\IN_OTPRAV\\"
        # Директория полученных файлов от ОПС
        self.dir_upload_files = u"C:\OPS_UPLOAD\\"
        # Директория с резервными файлами
        self.dir_res_files = self.script_dir + "reserve\\"
        # Директория для временной обработки файлов
        self.dir_work_files = self.script_dir + "work\\"

        # ["Название опции", "Параметр", "Описание"]
        self.config_list = [["num_base_ops", self.num_base_ops, u"Номер базового ОПС"],
                           ["dir_in_files", self.dir_in_files, u"Директория файлов на обработку"],
                           ["dir_out_files", self.dir_out_files, u"Директория файлов на отправку"],
                           ["dir_res_files", self.dir_res_files, u"Директория с резервными файлами"],
                           ["dir_work_files", self.dir_work_files, u"Директория для временной обработки файлов"],
                           ["dir_upload_files", self.dir_upload_files, u"Директория полученных файлов от ОПС"]]

        # Запрос создания таблицы настроек
        self.query_config_table = """
                create table %s (
                id integer not null primary key autoincrement,
                name text not null,
                param text not null,
                desc text
                );
                """ % self.table_name_config
        # Запрос на вставку данных настроек
        self.query_config_data = """insert into %s (name, param, desc) values (?, ?, ?)""" % self.table_name_config

    def create_config_table(self):
        """Создает таблицу настроек"""
        self._create_table(self.query_config_table)

    def insert_config_data(self):
        """Вставляет данные в таблицу настроек"""
        self._insert_data(self.query_config_data, self.config_list)