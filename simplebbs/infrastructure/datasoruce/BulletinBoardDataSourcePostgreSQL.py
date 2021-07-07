from simplebbs.infrastructure.datasoruce.postgresql_db import get_postgres
from simplebbs.infrastructure.repository.BulletinBoardRepository import BulletinBoardRepository


class BulletinBoardDataSourcePostgreSQL(BulletinBoardRepository):

    def queryThreadList(self) -> []:

        conn = get_postgres()
        c = conn.cursor()
        c.execute('SELECT * FROM threads ORDER BY thread_no DESC')
        rows = c.fetchall()
        thread_list = []
        for row in rows:
            thread_list.append([row[0], row[1]])
        c.close()

        return thread_list
