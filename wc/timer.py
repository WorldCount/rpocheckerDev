#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Измеряеn время работы чего-либо.
"""

__date__ = "18.03.2013"
__author__ = 'WorldCount'
__email__ = "world.count@yandex.ru"
__copyright__ = "Copyright 2013, Scr1pt1k.Ru"

import time


class Timer(object):

    """
    Изверяет время работы. Является менеджером контента.
    @author WorldCount
    @version 0.1
    @date 2014/03/31
    """
    
    def __init__(self, verbose=False):
        self.verbose = verbose
        self.start = ""
        self.end = ""
        self.secs = ""
        self.msecs = ""

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        
        self.end = time.time()
        self.secs = self.end - self.start
        self.msecs = self.secs * 1000  # millisecs
        
        if self.verbose:
            print u'Затраченное время: %f ms' % self.msecs