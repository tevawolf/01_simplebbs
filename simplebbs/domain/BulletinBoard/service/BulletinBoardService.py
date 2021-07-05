from datetime import datetime

from injector import Injector

from simplebbs.binds import BulletinBoardDIModule
from simplebbs.domain.BulletinBoard.factory import BulletinFactory
from simplebbs.domain.BulletinBoard.object.BulletinBoard import BulletinBoard


class BulletinBoardService:
    """
    初期起動表示
    投稿
    """

    @staticmethod
    def initDisplay() -> BulletinBoard:
        injector = Injector([BulletinBoardDIModule()])
        bulletin_board = injector.get(BulletinBoard)
        return bulletin_board

    @staticmethod
    def postBulletin(name: str, dt: datetime, title, text: str):

        bulletin = BulletinFactory.create(9999, name, dt, title, text)
        bulletin.createBulletin()
