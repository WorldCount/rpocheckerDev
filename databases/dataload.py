#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Загрузка данных из БД
"""

__date__ = "29.03.14"
__author__ = 'WorldCount'
__email__ = "world.count@yandex.ru"
__copyright__ = "Copyright 2014, Scr1pt1k.Ru"

from databases import dataquery
import datetime
import time


class DataLoad(dataquery.DataQuery):

    """
    Загрузка данных из БД
    @author WorldCount
    @version 0.1
    @date 2014/03/29
    """

    def __init__(self):
        dataquery.DataQuery.__init__(self)
        # Полученные данные
        self.data_list = []
        # Масква формата времени
        self.time_mask = "%d.%m.%Y"

    def gen_time_mask(self, date_in=False, date_out=False):
        """Возвращает список из 2-х штампов времени"""

        # Если начальной даты нету,
        if not date_in:
            # то будет сегодняшняя - 1 день.
            date_temp = datetime.datetime.today().strftime(self.time_mask)
            date_start = datetime.datetime.strptime(date_temp, self.time_mask) - datetime.timedelta(1)
        else:
            date_start = datetime.datetime.strptime(date_in, self.time_mask)

        # Если конечной даты нету
        if not date_out:
            # и нету начальной
            if not date_in:
                # то будет сгенерированная начальная дата + 47:59:59
                date_end = date_start + datetime.timedelta(1, 86399)
            else:
                # если же начальная есть, то начальная дата + 23:59:59
                date_end = date_start + datetime.timedelta(0, 86399)
        else:
            # если конечная дата есть, то конечная дата + 23:59:59
            date_end = datetime.datetime.strptime(date_out, self.time_mask) + datetime.timedelta(0, 86399)
        # Возвращаем даты в секундах
        return [int(time.mktime(date_start.timetuple())), int(time.mktime(date_end.timetuple()))]

    def load(self, number_ops = False, type_file=False, date_in=False, date_out=False, double=False):
        """Загружает данные файлов из БД"""
        pass