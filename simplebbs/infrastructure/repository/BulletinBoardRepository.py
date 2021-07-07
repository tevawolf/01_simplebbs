from abc import ABCMeta, abstractmethod


class BulletinBoardRepository(metaclass=ABCMeta):
    """
    @RepositotyInterface リポジトリインターフェース
    """

    @abstractmethod
    def queryThreadList(self) -> []:
        """
        BulletinBoardThreadのリストを返すクエリ―メソッド
        :return: BulletinBoardThreadのリスト
        """
        return []
