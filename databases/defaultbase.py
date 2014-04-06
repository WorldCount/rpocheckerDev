#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Пустая БД с начальными данными
"""

__date__ = "29.03.14"
__author__ = 'WorldCount'
__email__ = "world.count@yandex.ru"
__copyright__ = "Copyright 2014, Scr1pt1k.Ru"

import os
import sys
from databases import dataquery, dataparser, defaultconfig


class DefaultBase(dataquery.DataQuery, dataparser.DataParser, defaultconfig.DefaultConfig):

    """
    Создает БД с начальными данными
    @author WorldCount
    @version 0.1
    @date 2014/03/29
    """

    def __init__(self):

        dataquery.DataQuery.__init__(self)
        defaultconfig.DefaultConfig.__init__(self)

        # Файл с данными по МЖД
        self.ems_link = self.data_dir + "ems_data.wc"
        # Файл с данными по индексам
        self.index_link = self.data_dir + "index.wc"

        # Если базы нет, то создаем
        if not os.path.exists(self.base):
            self.create_database()

    def create_database(self):
        """Создает БД по-умолчанию"""
        print u"Создаю Базу..."

        with self.connect() as conn:

            curr = conn.cursor()

            # Таблицы для Почтовых Отправлений
            for name in self.table_name_post.values():
                curr.execute(self.query_ops_table % name)

            # Таблица для Международных
            curr.execute(self.query_ems_table)
            # Таблица для индексов
            curr.execute(self.query_index_table)
            # Таблица для настроек
            curr.execute(self.query_config_table)

            # Вставляем данные по EMS в БД
            ems_list = self.parse_ems(self.ems_link)
            curr.executemany(self.query_ems_data, ems_list)
             # Вставляем данные по индексам в БД
            index_list = self.parse_index(self.index_link)
            curr.executemany(self.query_index_data, index_list)
            # Вставляем данные по настрокам
            curr.executemany(self.query_config_data, self.config_list)

        print u"Создание завершено."

    def recreate_database(self):
        """Пересоздает базу данных"""
        try:
            os.remove(self.base)
        except WindowsError:
            print u"Ошибка! База открыта в другой программе."
            sys.exit(0)
        self.create_database()