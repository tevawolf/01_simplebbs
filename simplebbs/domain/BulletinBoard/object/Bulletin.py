from injector import inject

from simplebbs.infrastructure.repository import BulletinRepository
from simplebbs.domain.BulletinBoard.value import PostText
from simplebbs.domain.BulletinBoard.value.BulletinNo import BulletinNo
from simplebbs.domain.BulletinBoard.value.PostDateTime import PostDateTime
from simplebbs.domain.BulletinBoard.value.PosterName import PosterName


class Bulletin:
    """
    @DomainObject ドメインオブジェクト
    掲示物
    @EntityObject エンティティオブジェクト
    一意性のある掲示物を表す
    """

    @inject
    def __init__(self, r: BulletinRepository):
        self.repository = r
        self.bulletinNo = None
        self.posterName = None
        self.postDateTime = None
        self.postText = None

    def setValues(self, no: BulletinNo, name: PosterName, dt: PostDateTime, text: PostText):
        self.bulletinNo = no
        self.posterName = name
        self.postDateTime = dt
        self.postText = text

    def createBulletin(self) -> None:
        """
        掲示物を作成
        :return: なし
        """
        # 永続化
        self.repository.addBulletin(
            self.posterName.getValue(),
            self.postDateTime.getValue(),
            self.postText.getValue()
        )
