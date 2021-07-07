from simplebbs.infrastructure.datasoruce.postgresql_db import get_postgres
from simplebbs.infrastructure.repository.BulletinBoardThreadRepository import BulletinBoardThreadRepository


class BulletinBoardThreadDataSourcePostgreSQL(BulletinBoardThreadRepository):

    def queryBulletinList(self, no: int) -> []:

        conn = get_postgres()
        c = conn.cursor()
        c.execute('SELECT * FROM bulletins WHERE thread_no = {0} ORDER BY bulletin_no DESC'.format(no))
        rows = c.fetchall()
        bulletin_list = []
        for row in rows:
            bulletin_list.append([row[0], row[1], row[2], row[4], row[3], row[5]])
        c.close()

        return bulletin_list

    def createThread(self, name: str) -> bool:

        # DB接続、SQL実行とコミット
        conn = get_postgres()
        c = conn.cursor()

        c.execute("""SELECT MAX(thread_no) FROM threads""")
        no = c.fetchone()[0] + 1

        c.execute("""INSERT INTO threads(thread_no, thread_name)
                    VALUES ({0}, '{1}')""".format(no, name))
        conn.commit()

        c.close()
        return True
