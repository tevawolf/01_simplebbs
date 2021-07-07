from abc import ABCMeta, abstractmethod


class BulletinBoardThreadRepository(metaclass=ABCMeta):
    """
    @RepositotyInterface リポジトリインターフェース
    """

    @abstractmethod
    def queryBulletinList(self, no: int) -> []:
        """
        Bulletinのリストを返すクエリ―メソッド
        :return: Bulletinのリスト
        """
        return []

    @abstractmethod
    def createThread(self, name: str) -> bool:
        """
        BulletinBoardThreadを永続化するメソッド
        :param name:
        :return:
        """
        pass