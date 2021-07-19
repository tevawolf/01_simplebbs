import psycopg2
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from simplebbs.infrastructure.datasoruce.postgresql_db import get_postgres
from simplebbs.infrastructure.repository.PosterRepository import PosterRepository


class PosterDataSourcePostgreSQL(PosterRepository):

    def addPoster(self, id: str, name: str, password: bytes, tag: bytes, nonce: bytes) -> bool:

        # DB接続、SQL実行とコミット
        conn = get_postgres()
        c = conn.cursor()
        c.execute(r"INSERT INTO posters(poster_id, poster_name, password, tag, nonce) VALUES " \
                      "('{0}', '{1}'".format(id, name) + ", %s, %s, %s )",
                  (psycopg2.Binary(password), psycopg2.Binary(tag), psycopg2.Binary(nonce),)
                  )
        conn.commit()

        c.close()
        return True

    def queryPoster(self, poster_id: str) -> []:

        poster = []

        conn = get_postgres()
        c = conn.cursor()
        c.execute("SELECT * FROM posters WHERE poster_id = '{0}'".format(poster_id))
        row = c.fetchone()

        if not (row is None):
            poster.append(row[0])
            poster.append(row[1])
            poster.append(row[2])
            poster.append(row[3])
            poster.append(row[4])
            c.close()

        return poster
