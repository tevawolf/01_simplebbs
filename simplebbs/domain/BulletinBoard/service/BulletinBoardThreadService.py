from datetime import datetime

from simplebbs.domain.BulletinBoard.factory import BulletinFactory
from simplebbs.domain.BulletinBoard.factory.BulletinBoardThreadFactory import BulletinBoardThreadFactory
from simplebbs.domain.BulletinBoard.object.BulletinBoardThread import BulletinBoardThread


class BulletinBoardThreadService:
    """
    掲示板スレッド表示
    投稿
    """

    @staticmethod
    def displayThread(no: int, name: str) -> BulletinBoardThread:
        thread = BulletinBoardThreadFactory.create(no, name)
        thread.setBulletinList()
        return thread

    @staticmethod
    def postBulletin(name: str, dt: datetime, title, text: str, thread_no: int) -> None:

        bulletin = BulletinFactory.create(9999, name, dt, title, text, thread_no)
        bulletin.createBulletin()
