from abc import ABCMeta, abstractmethod
from datetime import datetime


class BulletinRepository(metaclass=ABCMeta):
    """
    @RepositoryInterface
    """

    @abstractmethod
    def addBulletin(self, name: str, dt: datetime, title: str, text: str) -> bool:
        """
        Bulletinを永続化するメソッド
        :param title:
        :param text:
        :param dt:
        :param name:
        :return:
        """
        pass
