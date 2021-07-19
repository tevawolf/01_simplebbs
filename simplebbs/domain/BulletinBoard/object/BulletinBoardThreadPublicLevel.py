import enum


@enum.unique
class BulletinBoardThreadPublicLevel(enum.Enum):
    """
    @DomainObject 掲示板スレッド公開レベル
    """
    公開 = 1
    閲覧のみ = 2
    非公開 = 3

