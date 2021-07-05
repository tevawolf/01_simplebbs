from typing import Union

from simplebbs.domain.BulletinBoard.factory.PosterFactory import PosterFactory


class PosterService:
    """
    サインアップ
    サインイン
    """

    @staticmethod
    def signUp(id: str, name: str, password: str) -> None:
        poster = PosterFactory.create(id, name, password)
        poster.createPoster()

    @staticmethod
    def signIn(id: str, password: str) -> Union[bool, str]:
        poster = PosterFactory.create(id, ' ', password)  # PosterNameにはダミーをセット
        return poster.authenticatePoster()
