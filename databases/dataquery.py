#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Основные запросы для создания БД
"""

__date__ = "29.03.14"
__author__ = 'WorldCount'
__email__ = "world.count@yandex.ru"
__copyright__ = "Copyright 2014, Scr1pt1k.Ru"

from databases import database


class DataQuery(database.DataBase):

    """
    Запросы для создания БД
    @author WorldCount
    @version 0.1
    @date 2014/03/29
    """

    def __init__(self):

        database.DataBase.__init__(self)

        # Название таблицы ОПС
        self.table_name_ems = "Trans"
        # Название таблицы индексов
        self.table_name_index = "PostIndex"
        # Названия таблиц с отправлениями
        self.table_name_post = {"W": "WinPost", "P": "PartPost", "D": "DW",
                                "R": "Sort", "N": "NW", "B": "BaseOps", "U": "Unkown"}
        #self.tableNamePost = ["WinPost", "PartPost", "DW", "Sort", "Post", "BaseOps", "Unkown"]

        # Запрос для таблиц ОПС
        self.query_ops_table = """
                create table %s(
                id integer not null primary key autoincrement,
                num_file text not null,
                num_ops integer not null,
                file_date_stamp real not null,
                file_hash text not null,
                dup integer null,
                file_soft text not null,
                num_string integer,
                num_error integer,
                wid text
                );
                """

        # Запрос для таблицы EMS
        self.query_ems_table = """
                create table %s(
                flag  text not null primary key,
                runame text not null,
                enname text not null,
                code integer null
                );
                """ % self.table_name_ems

        # Запрос для таблицы индексов
        self.query_index_table = """
                create table %s(
                code  text not null primary key,
                city text not null,
                region text not null
                );
                """ % self.table_name_index

        # Запросы на вставку данных
        self.query_ems_data = """insert into %s (flag, runame, enname, code) values (?, ?, ?, ?)""" % self.table_name_ems
        self.query_index_data = """insert into %s (code, city, region) values (?, ?, ?)""" % self.table_name_index

    def create_ops_tables(self, tables_names=0):
        """Создает таблицы ОПС"""
        if tables_names == 0:
            tables_names = self.table_name_post
        with self.connect() as conn:
            curr = conn.cursor()
            for name in tables_names.values():
                curr.execute(self.query_ops_table % name)

    def create_ems_table(self):
        """Создает таблицу с EMS"""
        self._create_table(self.query_ems_table)

    def create_index_table(self):
        """Создает таблицу с индексами"""
        self._create_table(self.query_index_table)

    def insert_ems_data(self, ems_list=0):
        """Вставляет данные в таблицу EMS"""
        self._insert_data(self.query_ems_data, ems_list)

    def insert_index_data(self, index_list=0):
        """Вставляет данные в таблицу индексов"""
        self._insert_data(self.query_index_data, index_list)
