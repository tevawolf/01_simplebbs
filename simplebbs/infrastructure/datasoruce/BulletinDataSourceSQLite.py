from datetime import datetime

from simplebbs.infrastructure.datasoruce.sqlite_db import get_db
from simplebbs.infrastructure.repository.BulletinRepository import BulletinRepository


class BulletinDataSourceSQLite(BulletinRepository):

    def addBulletin(self, name: str, dt: datetime, text: str) -> bool:

        # DB接続、SQL実行とコミット
        conn = get_db()
        c = conn.cursor()

        c.execute("""SELECT MAX(bulletin_no) FROM bulletins""")
        no = c.fetchone()[0] + 1

        # textの改行コードに対応
        text = text.replace('\r\n', '<br>')

        c.execute("""INSERT INTO bulletins(bulletin_no, poster_name, post_datetime, post_text)
                    VALUES ({0}, '{1}', '{2}', '{3}')""".format(no, name, dt, text))
        conn.commit()

        c.close()
        return True
