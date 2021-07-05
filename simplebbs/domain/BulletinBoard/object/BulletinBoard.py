import copy

from injector import inject

from simplebbs.domain.BulletinBoard.factory import BulletinFactory
from simplebbs.domain.BulletinBoard.object.Bulletin import Bulletin
from simplebbs.infrastructure.repository import BulletinBoardRepository


class BulletinBoard:
    """
    @DomainObject 掲示板
    @CollectionObject 掲示物のコレクション
    """
    @inject
    def __init__(self, r: BulletinBoardRepository):
        self.bulletins = []

        # こちらでクエリ発行して、まず全件保持しておく
        builtin_list = r.queryBulletinList()
        for b in builtin_list:
            bulletin = BulletinFactory.create(b[0], b[1], b[2], b[3], b[4])
            self.bulletins.append(bulletin)

    def postAllBulletins(self) -> [Bulletin]:
        """
        掲示物をすべて掲示する
        :return
        """
        return copy.deepcopy(self.bulletins)
