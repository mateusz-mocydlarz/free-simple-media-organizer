# -*- coding: utf-8 -*-
import sqlite3


def connect_sqlite(path_to_db):
    con = sqlite3.connect(path_to_db)
    con.execute('PRAGMA foreign_keys = ON')

    return con
