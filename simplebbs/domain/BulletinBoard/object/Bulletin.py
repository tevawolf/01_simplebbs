from injector import inject

from simplebbs.domain.BulletinBoard.value.PostTitle import PostTitle
from simplebbs.domain.BulletinBoard.value.ThreadNo import ThreadNo
from simplebbs.infrastructure.repository import BulletinRepository
from simplebbs.domain.BulletinBoard.value import PostText
from simplebbs.domain.BulletinBoard.value.BulletinNo import BulletinNo
from simplebbs.domain.BulletinBoard.value.PostDateTime import PostDateTime
from simplebbs.domain.BulletinBoard.value.PosterName import PosterName


class Bulletin:
    """
    @DomainObject 掲示物
    @EntityObject （一意性のある）掲示物を表す
    """

    @inject
    def __init__(self, r: BulletinRepository):
        self.repository = r
        self.bulletinNo = None
        self.posterName = None
        self.postDateTime = None
        self.postTitle = None
        self.postText = None
        self.thread_no = None

    def setValues(self, no: BulletinNo, name: PosterName, dt: PostDateTime, title: PostTitle, text: PostText, thread_no: ThreadNo):
        self.bulletinNo = no
        self.posterName = name
        self.postDateTime = dt
        self.postTitle = title
        self.postText = text
        self.thread_no = thread_no

    def createBulletin(self) -> None:
        """
        掲示物を作成
        :return: なし
        """
        # 永続化
        self.repository.addBulletin(
            self.posterName.getValue(),
            self.postDateTime.getValue(),
            self.postTitle.getValue(),
            self.postText.getValue(),
            self.thread_no.getValue()
        )
