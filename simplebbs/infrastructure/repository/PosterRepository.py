from abc import ABCMeta, abstractmethod


class PosterRepository(metaclass=ABCMeta):
    """
    @RepositoryInterface
    """

    @abstractmethod
    def addPoster(self, posterid: str, name: str, password: bytes, tag: bytes, nonce: bytes) -> bool:
        """
        Posterを永続化するメソッド
        :param posterid:
        :param name:
        :param password:
        :return:
        """
        pass

    @abstractmethod
    def getPoster(self, poster_id: str) -> []:
        """
        Posterのデータを取得するメソッド
        :param poster_id:
        :return: Posterデータリスト
        """
        pass
