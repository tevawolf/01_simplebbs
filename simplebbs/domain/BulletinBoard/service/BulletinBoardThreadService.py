from datetime import datetime

from simplebbs.domain.BulletinBoard.factory import BulletinFactory
from simplebbs.domain.BulletinBoard.factory.BulletinBoardThreadFactory import BulletinBoardThreadFactory
from simplebbs.domain.BulletinBoard.object.BulletinBoardThread import BulletinBoardThread
from simplebbs.domain.BulletinBoard.object.BulletinBoardThreadPublicLevel import BulletinBoardThreadPublicLevel


class BulletinBoardThreadService:
    """
    掲示板スレッド表示
    投稿
    パスワード認証
    """

    @staticmethod
    def displayThread(no: int) -> BulletinBoardThread:
        # 公開レベルもダミー
        thread = BulletinBoardThreadFactory.create(no, 'dummy', BulletinBoardThreadPublicLevel.公開, 'dummy')
        thread.setValuesByRepository()
        thread.setBulletinList()
        return thread

    @staticmethod
    def postBulletin(name: str, dt: datetime, title, text: str, thread_no: int) -> None:

        bulletin = BulletinFactory.create(9999, name, dt, title, text, thread_no)
        bulletin.createBulletin()

    @staticmethod
    def authenticatePassword(no: int, password: str) -> bool:
        # 公開レベルもダミー
        thread = BulletinBoardThreadFactory.create(no, 'dummy', BulletinBoardThreadPublicLevel.公開, password)
        return thread.isPasswordMatched()
