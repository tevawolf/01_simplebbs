from simplebbs.infrastructure.datasoruce.postgresql_db import get_postgres
from simplebbs.infrastructure.repository.BulletinBoardRepository import BulletinBoardRepository


class BulletinBoardDataSourcePostgreSQL(BulletinBoardRepository):

    def queryBulletinList(self) -> []:

        conn = get_postgres()
        c = conn.cursor()
        c.execute('SELECT * FROM bulletins ORDER BY bulletin_no DESC')
        rows = c.fetchall()
        bulletin_list = []
        for row in rows:
            bulletin_list.append([row[0], row[1], row[2], row[3]])
        c.close()

        return bulletin_list
