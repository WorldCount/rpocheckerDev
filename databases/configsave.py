#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Сохранение конфига в БД
"""

__date__ = "29.03.14"
__author__ = 'WorldCount'
__email__ = "world.count@yandex.ru"
__copyright__ = "Copyright 2014, Scr1pt1k.Ru"

from databases import defaultconfig


class ConfigSave(defaultconfig.DefaultConfig):

    """
    Сохраняет настройки в БД
    @author WorldCount
    @version 0.1
    @date 2014/03/29
    """

    def __init__(self):
        defaultconfig.DefaultConfig.__init__(self)