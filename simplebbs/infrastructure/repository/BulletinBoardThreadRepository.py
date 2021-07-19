from abc import ABCMeta, abstractmethod


class BulletinBoardThreadRepository(metaclass=ABCMeta):
    """
    @RepositotyInterface リポジトリインターフェース
    """
    @abstractmethod
    def queryThread(self, no: int) -> []:
        """
        noに一致するThreadを返すクエリ―メソッド
        :param no: スレッドNo
        :return: Thread
        """
        pass

    @abstractmethod
    def queryBulletinList(self, no: int) -> []:
        """
        Bulletinのリストを返すクエリーメソッド
        :return: Bulletinのリスト
        """
        return []

    @abstractmethod
    def createThread(self, name: str, level: int, password: str) -> bool:
        """
        BulletinBoardThreadを永続化するメソッド
        :param name:
        :return:
        """
        pass

    @abstractmethod
    def queryThreadPassword(self, no: int) -> str:
        """
        BulletinBoardThreadに設定されたパスワードを返すクエリーメソッド
        :param no:
        :param password:
        :return:
        """
        pass