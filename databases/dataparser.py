#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Парсер данных для БД
"""

__date__ = "29.03.14"
__author__ = 'WorldCount'
__email__ = "world.count@yandex.ru"
__copyright__ = "Copyright 2014, Scr1pt1k.Ru"

import os
import csv
from databases import dataerror


class DataParser(object):

    """
    Парсер данных для БД
    @author WorldCount
    @version 0.1
    @date 2014/03/29
    """

    def parse_ems(self, link_ems_data):
        """Парсит данные по МЖД"""
        if not os.path.exists(link_ems_data):
            raise dataerror.DataFileNotFound("EMS", link_ems_data)
        with open(link_ems_data, 'rb') as ems_list:
            data_list = csv.reader(ems_list, delimiter = "|", quotechar="\n")
            result = list(data_list)
        for mystr in result:
            mystr[1] = mystr[1].decode("utf-8")
        return result

    def parse_index(self, link_index_data):
        """Парсит данные по МЖД"""
        if not os.path.exists(link_index_data):
            raise dataerror.DataFileNotFound("Index", link_index_data)
        with open(link_index_data, 'rb') as index_list:
            data_list = csv.reader(index_list, delimiter = ";", quotechar="\n")
            result = list(data_list)
        for mystr in result:
            #myStr[0] = myStr[0]
            mystr[1] = mystr[1].decode("utf-8")
            mystr[2] = mystr[2].decode("utf-8")
        return result