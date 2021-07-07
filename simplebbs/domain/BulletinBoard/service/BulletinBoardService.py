from injector import Injector

from simplebbs.binds import BulletinBoardDIModule
from simplebbs.domain.BulletinBoard.factory.BulletinBoardThreadFactory import BulletinBoardThreadFactory
from simplebbs.domain.BulletinBoard.object.BulletinBoard import BulletinBoard


class BulletinBoardService:
    """
    初期起動表示
    スレッド作成
    """

    @staticmethod
    def initDisplay() -> BulletinBoard:
        injector = Injector([BulletinBoardDIModule()])
        bulletin_board = injector.get(BulletinBoard)
        return bulletin_board

    @staticmethod
    def createThread(name: str) -> None:
        thread = BulletinBoardThreadFactory.create(9999, name)
        thread.createThread()
