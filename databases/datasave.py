#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Ошибки при работе с БД
"""

__date__ = "29.03.14"
__author__ = 'WorldCount'
__email__ = "world.count@yandex.ru"
__copyright__ = "Copyright 2014, Scr1pt1k.Ru"

from databases import dataquery


class DataSave(dataquery.DataQuery):

    """
    Сохраняет данные по РПО в базу
    @author WorldCount
    @version 0.1
    @date 2014/03/29
    """

    def __init__(self):
        dataquery.DataQuery.__init__(self)

        # Запрос для сохранения данных в БД
        self.query_ops_data = """insert into %s (num_file, num_ops, file_date_stamp, file_hash, dup, file_soft, num_string, num_error, wid)
         values (?, ?, ?, ?, ?, ?, ?, ?, ?)"""

        # СПИСКИ С ДАННЫМИ
        self.data_base_list = []      # Базовые файлы
        self.data_part_list = []      # Партионка
        self.data_win_list = []       # ВинПост
        self.data_sort_list = []      # Сортировочный узел
        self.data_nw_list = []        # Почтовые отправления
        self.data_dw_list = []        # Доставка
        self.data_unkown_list = []    # Неизвестные

        # СЧЕТЧИКИ ФАЙЛОВ
        self.count_all_files = 0      # Всего файлов
        self.count_dup_files = 0      # Дубликатов
        self.count_new_files = 0      # Новых

    def get_file_type(self, fileobject):
        """Возращает тип файла"""
        version = fileobject.version[:1]
        return self.table_name_post.get(version, self.table_name_post["U"])

    def add_base(self, fileobject):
        """Собирает списки с данными файлов"""
        self.count_all_files += 1

        # Получаем тип файла
        file_type = self.get_file_type(fileobject)
        fileobject.file_type = file_type

        with self.connect() as conn:
            curr = conn.cursor()
            # Запрос для проверки на дубликат
            query = "select file_hash from %s where file_hash = ? and num_file = ? limit 1" % file_type
            curr.execute(query, (fileobject.hash, fileobject.name,))
            if len(curr.fetchall()) > 0:
                fileobject.double = True
                self.count_dup_files += 1
            else:
                fileobject.double = False
                self.count_new_files += 1
        # Заносим данные
        temp_tuple = (fileobject.name, fileobject.ops_number, fileobject.date_file, fileobject.hash,
                      fileobject.double, fileobject.version, fileobject.sum_string, fileobject.error, fileobject.window)
        # Добавляем данные в списки по типу файла
        if fileobject.file_type == self.table_name_post["B"]:
            self.data_base_list.append(temp_tuple)
        elif fileobject.file_type == self.table_name_post["W"]:
            self.data_win_list.append(temp_tuple)
        elif fileobject.file_type == self.table_name_post["P"]:
            self.data_part_list.append(temp_tuple)
        elif fileobject.file_type == self.table_name_post["D"]:
            self.data_dw_list.append(temp_tuple)
        elif fileobject.file_type == self.table_name_post["R"]:
            self.data_sort_list.append(temp_tuple)
        elif fileobject.file_type == self.table_name_post["N"]:
            self.data_nw_list.append(temp_tuple)
        else:
            self.data_unkown_list.append(temp_tuple)

    def save(self):
        """Сохраняет данные в БД"""

        # Формируем запросы
        query1 = self.query_ops_data % self.table_name_post["B"]
        query2 = self.query_ops_data % self.table_name_post["W"]
        query3 = self.query_ops_data % self.table_name_post["P"]
        query4 = self.query_ops_data % self.table_name_post["D"]
        query5 = self.query_ops_data % self.table_name_post["R"]
        query6 = self.query_ops_data % self.table_name_post["N"]
        query7 = self.query_ops_data % self.table_name_post["U"]
        with self.connect() as conn:
            curr = conn.cursor()
            # Выполняем запросы
            curr.executemany(query1, self.data_base_list)
            curr.executemany(query2, self.data_win_list)
            curr.executemany(query3, self.data_part_list)
            curr.executemany(query4, self.data_dw_list)
            curr.executemany(query5, self.data_sort_list)
            curr.executemany(query6, self.data_nw_list)
            curr.executemany(query7, self.data_unkown_list)
        # Чистим списки
        self.data_base_list = []
        self.data_win_list = []
        self.data_part_list = []
        self.data_dw_list = []
        self.data_sort_list = []
        self.data_nw_list = []
        self.data_unkown_list = []

    def get_count_files(self):
        """Возвращает список со счетчиками файлов"""
        return [self.count_all_files, self.count_dup_files, self.count_new_files]



