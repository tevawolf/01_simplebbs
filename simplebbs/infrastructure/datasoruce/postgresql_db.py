import os

import psycopg2
from flask import g

DATABASE_HEROKU = 'host=' + str(os.environ.get('DATABASE_URL')) + ' port=5432' + \
           ' dbname=d4o6thnl90bnmp' + \
           ' user=vokuyzrqbczpmk' + \
           ' password=c4f68a9ff954e2cedb70673c5bc22fddf16b67be50b948ee8616acc93413e5dd'

DATABASE_LOCAL = 'host=127.0.0.1 port=5432 dbname=warewolf user=tevawolf password=teVa0210'


def get_postgres():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = psycopg2.connect(DATABASE_HEROKU)
        # db = g._database = psycopg2.connect(DATABASE_LOCAL)
    return db


def close_postgres_connection(exception=None):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
