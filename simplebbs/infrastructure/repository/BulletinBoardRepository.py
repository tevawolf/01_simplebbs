from abc import ABCMeta, abstractmethod


class BulletinBoardRepository(metaclass=ABCMeta):
    """
    @RepositotyInterface リポジトリインターフェース
    """

    @abstractmethod
    def queryBulletinList(self) -> []:
        """
        Bulletinのリストを返すクエリ―メソッド
        :return: Bulletinのリスト
        """
        return []
