#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Проверка индексов и EMS
"""

__date__ = "29.03.14"
__author__ = 'WorldCount'
__email__ = "world.count@yandex.ru"
__copyright__ = "Copyright 2014, Scr1pt1k.Ru"

from databases import dataquery


class DataCheck(dataquery.DataQuery):

    """
    Проверка данных EMS и индексов в БД
    @author WorldCount
    @version 0.1
    @date 2014/03/29
    """

    def __init__(self):
        dataquery.DataQuery.__init__(self)

    def search_ems_code(self, value):
        """Ищет данные по EMS в БД"""
        query = "select code from %s where flag = ?" % self.table_name_ems
        with self.connect() as conn:
            curr = conn.cursor()
            curr.execute(query, (value,))
            response = list(curr.fetchall())
            if len(response) < 1:
                return False
            else:
                return response[0][0]

    def search_index_code(self, value):
        """Ищет данные по индексу в БД"""
        if len(value) < 6:
            return False
        query = "select code from %s where code = ?" % self.table_name_index
        with self.connect() as conn:
            curr = conn.cursor()
            curr.execute(query, (value,))
            response = list(curr.fetchall())
            if len(response) < 1:
                return False
            else:
                return True

    def search_index_data(self, value):
        """Ищет ближние индексы в БД"""
        query = "select code from %s where code like ?" % self.table_name_index
        if value[0:1] != "%" and value[-1:len(value)] != "%":
            value = '%' + value + '%'
        with self.connect() as conn:
            curr = conn.cursor()
            curr.execute(query, (value,))
            response = list(curr.fetchall())
            if len(response) < 1:
                return False
            else:
                result = [line[0] for line in response]
                return result