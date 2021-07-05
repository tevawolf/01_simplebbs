from datetime import datetime

from simplebbs.infrastructure.datasoruce.postgresql_db import get_postgres
from simplebbs.infrastructure.repository.BulletinRepository import BulletinRepository


class BulletinDataSourcePostgreSQL(BulletinRepository):

    def addBulletin(self, name: str, dt: datetime, title: str, text: str) -> bool:

        # DB接続、SQL実行とコミット
        conn = get_postgres()
        c = conn.cursor()

        c.execute("""SELECT MAX(bulletin_no) FROM bulletins""")
        no = c.fetchone()[0] + 1

        # textの改行コードに対応
        text = text.replace('\r\n', '<br>')

        c.execute("""INSERT INTO bulletins(bulletin_no, poster_name, post_datetime, post_text, post_title)
                    VALUES ({0}, '{1}', '{2}', '{3}', '{4}')""".format(no, name, dt, text, title))
        conn.commit()

        c.close()
        return True
