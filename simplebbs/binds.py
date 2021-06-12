from injector import Module, Binder

from simplebbs.infrastructure.datasoruce.BulletinBoardDataSourceSQLite import BulletinBoardDataSourceSQLite
from simplebbs.infrastructure.datasoruce.BulletinDataSourceSQLite import BulletinDataSourceSQLite
from simplebbs.infrastructure.repository.BulletinBoardRepository import BulletinBoardRepository
from simplebbs.infrastructure.repository.BulletinRepository import BulletinRepository


class BulletinBoardDIModule(Module):

    def configure(self, binder: Binder):
        binder.bind(BulletinBoardRepository, to=BulletinBoardDataSourceSQLite)
        binder.bind(BulletinRepository, to=BulletinDataSourceSQLite)
