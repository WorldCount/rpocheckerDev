#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Загрузка конфига из БД
"""

__date__ = "29.03.14"
__author__ = 'WorldCount'
__email__ = "world.count@yandex.ru"
__copyright__ = "Copyright 2014, Scr1pt1k.Ru"

from databases import defaultconfig
from databases import dataerror

class ConfigLoad(defaultconfig.DefaultConfig):

    """
    Загружает настройки из БД
    @author WorldCount
    @version 0.1
    @date 2014/03/29
    """

    def __init__(self):
        defaultconfig.DefaultConfig.__init__(self)

        # Запрос на получение опции из настроек
        self.query_get_option = u"""select param from %s where name = ?""" % self.table_name_config

    def load_option(self, value):
        """Загружает опцию из настроек"""
        if value != "":
            with self.connect() as conn:
                curr = conn.cursor()
                curr.execute(self.query_get_option,(value,))
                response = list(curr.fetchall())
                if len(response) < 1:
                    return False
                else:
                    return response[0][0]
        else:
            dataerror.ParamError("value", "loadOption(self, value)")


