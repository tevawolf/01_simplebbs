from simplebbs.infrastructure.datasoruce.sqlite_db import get_sqlite
from simplebbs.infrastructure.repository.BulletinBoardRepository import BulletinBoardRepository


class BulletinBoardDataSourceSQLite(BulletinBoardRepository):

    def queryBulletinList(self) -> []:

        conn = get_sqlite()
        c = conn.cursor()
        c.execute('SELECT * FROM bulletins ORDER BY bulletin_no DESC')
        rows = c.fetchall()
        bulletin_list = []
        for row in rows:
            bulletin_list.append([row[0], row[1], row[2], row[4], row[3]])
        c.close()

        return bulletin_list
