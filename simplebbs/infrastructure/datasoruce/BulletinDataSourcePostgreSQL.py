from datetime import datetime

from simplebbs.infrastructure.datasoruce.postgresql_db import get_postgres
from simplebbs.infrastructure.repository.BulletinRepository import BulletinRepository


class BulletinDataSourcePostgreSQL(BulletinRepository):

    def addBulletin(self, name: str, dt: datetime, title: str, text: str, thread_no: int) -> bool:

        # DB接続、SQL実行とコミット
        conn = get_postgres()
        c = conn.cursor()

        c.execute("""SELECT MAX(bulletin_no) FROM bulletins WHERE thread_no = {0}""".format(thread_no))
        no = c.fetchone()[0]
        if not (no is None):
            no = no + 1
        else:
            no = 1

        # textの改行コードに対応
        text = text.replace('\r\n', '<br>')

        c.execute("""INSERT INTO bulletins(bulletin_no, poster_name, post_datetime, post_text, post_title, thread_no)
                    VALUES ({0}, '{1}', '{2}', '{3}', '{4}', '{5}')""".format(no, name, dt, text, title, thread_no))
        conn.commit()

        c.close()
        return True
