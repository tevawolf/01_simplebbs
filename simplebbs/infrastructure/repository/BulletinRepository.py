from abc import ABCMeta, abstractmethod
from datetime import datetime


class BulletinRepository(metaclass=ABCMeta):
    """
    @RepositoryInterface リポジトリインターフェース
    """

    @abstractmethod
    def addBulletin(self, name: str, dt: datetime, text: str) -> bool:
        """
        Bulletinを永続化するメソッド
        :param text:
        :param dt:
        :param name:
        :return:
        """
        pass
