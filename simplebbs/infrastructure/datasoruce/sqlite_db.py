import sqlite3
from flask import g

DATABASE = 'simplebbs.db'


def get_sqlite():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


def close_sqlite_connection(exception=None):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
