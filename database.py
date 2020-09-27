from flask import g
import sqlite3


def connectdb():
    sql = sqlite3.connect('questions.db')
    sql.row_factory = sqlite3.Row
    return sql
def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connectdb()
    return g.sqlite_db
