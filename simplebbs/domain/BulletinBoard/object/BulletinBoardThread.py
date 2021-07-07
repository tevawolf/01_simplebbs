import copy

from injector import inject

from simplebbs.domain.BulletinBoard.factory import BulletinFactory
from simplebbs.domain.BulletinBoard.object.Bulletin import Bulletin
from simplebbs.domain.BulletinBoard.value.ThreadName import ThreadName
from simplebbs.domain.BulletinBoard.value.ThreadNo import ThreadNo
from simplebbs.infrastructure.repository.BulletinBoardThreadRepository import BulletinBoardThreadRepository


class BulletinBoardThread:
    """
    @DomainObject 掲示板スレッド
    @EntityObject （一意性のある）掲示板スレッドを表す
    @CollectionObject 掲示物のコレクション TODO 単独でコレクションオブジェクトをつくり、それをこのクラスに持たせるべきか？
    """
    @inject
    def __init__(self, r: BulletinBoardThreadRepository):
        self.repository = r
        self.thread_no = None
        self.thread_name = None
        self.bulletins = []

    def setValues(self, no: ThreadNo, name: ThreadName):
        self.thread_no = no
        self.thread_name = name

    def setBulletinList(self):
        builtin_list = self.repository.queryBulletinList(self.thread_no.getValue())
        for b in builtin_list:
            bulletin = BulletinFactory.create(b[0], b[1], b[2], b[3], b[4], b[5])
            self.bulletins.append(bulletin)

    def postAllBulletins(self) -> [Bulletin]:
        """
        掲示物をすべて掲示する
        :return
        """
        return copy.deepcopy(self.bulletins)

    def createThread(self) -> None:
        """
        掲示板スレッドを作成
        :return: なし
        """
        # 永続化
        self.repository.createThread(
            self.thread_name.getValue()
        )