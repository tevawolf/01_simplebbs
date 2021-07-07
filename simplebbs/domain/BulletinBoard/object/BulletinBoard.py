import copy

from injector import inject

from simplebbs.domain.BulletinBoard.factory import BulletinFactory
from simplebbs.domain.BulletinBoard.factory.BulletinBoardThreadFactory import BulletinBoardThreadFactory
from simplebbs.domain.BulletinBoard.object.BulletinBoardThread import BulletinBoardThread
from simplebbs.infrastructure.repository import BulletinBoardRepository


class BulletinBoard:
    """
    @DomainObject 掲示板
    @CollectionObject 掲示物スレッドのコレクション
    """
    @inject
    def __init__(self, r: BulletinBoardRepository):
        self.threads = []

        # こちらでクエリ発行して、まず全件保持しておく
        thread_list = r.queryThreadList()
        for b in thread_list:
            thread = BulletinBoardThreadFactory.create(b[0], b[1])
            self.threads.append(thread)

    def postAllThreads(self) -> [BulletinBoardThread]:
        """
        掲示板スレッドをすべて表示する
        :return
        """
        return copy.deepcopy(self.threads)