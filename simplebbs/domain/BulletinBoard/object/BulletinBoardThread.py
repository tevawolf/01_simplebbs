import copy

from injector import inject

from simplebbs.domain.BulletinBoard.factory import BulletinFactory
from simplebbs.domain.BulletinBoard.object.Bulletin import Bulletin
from simplebbs.domain.BulletinBoard.object.BulletinBoardThreadPublicLevel import BulletinBoardThreadPublicLevel
from simplebbs.domain.BulletinBoard.value.ThreadName import ThreadName
from simplebbs.domain.BulletinBoard.value.ThreadNo import ThreadNo
from simplebbs.domain.BulletinBoard.value.ThreadPassword import ThreadPassword
from simplebbs.infrastructure.repository.BulletinBoardThreadRepository import BulletinBoardThreadRepository


class BulletinBoardThread:
    """
    @DomainObject 掲示板スレッド
    @EntityObject （一意性のある）掲示板スレッドを表す
    @CollectionObject 掲示物のコレクション FIXME 単独でコレクションオブジェクトをつくり、それをこのクラスに持たせるべきか？
    """
    @inject
    def __init__(self, r: BulletinBoardThreadRepository):
        self.repository = r
        self.thread_no = None
        self.thread_name = None
        self.public_level = None
        self.password = None
        self.bulletins = []

    def setValues(self, no: ThreadNo, name: ThreadName, level: BulletinBoardThreadPublicLevel, password: ThreadPassword) -> None:
        """
        セッターメソッド
        :param no:　スレッドNo.
        :param name:　スレッド名
        :param level:　公開レベル
        :param password: スレッドパスワード
        :return: なし
        """
        self.thread_no = no
        self.thread_name = name
        self.public_level = level
        self.password = password

    def setValuesByRepository(self) -> None:
        """
        DB取得値をセット
        :return: なし
        """
        thread = self.repository.queryThread(self.thread_no.getValue())
        self.thread_name = ThreadName(thread[0])
        self.public_level = BulletinBoardThreadPublicLevel(int(thread[1]))

    def setBulletinList(self):
        """
        リポジトリから掲示物のリストを取得し、保持する
        :return: なし
        """
        builtin_list = self.repository.queryBulletinList(self.thread_no.getValue())
        for b in builtin_list:
            bulletin = BulletinFactory.create(b[0], b[1], b[2], b[3], b[4], b[5])
            self.bulletins.append(bulletin)

    def postAllBulletins(self) -> [Bulletin]:
        """
        掲示物をすべて掲示する
        :return　掲示物リストのコピー
        """
        return copy.deepcopy(self.bulletins)

    def createThread(self) -> None:
        """
        掲示板スレッドを作成
        :return: なし
        """
        # 永続化
        self.repository.createThread(
            self.thread_name.getValue(),
            self.public_level.value,
            self.password.getValue()
        )

    def isPasswordMatched(self) -> bool:
        """
        掲示板スレッドに設定されたパスワードと入力値が一致するか判定
        :param password:　パスワード
        :return:　判定結果
        """
        db_password = self.repository.queryThreadPassword(self.thread_no.getValue())
        return self.password.getValue() == db_password
