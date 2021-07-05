from injector import Injector

from simplebbs.binds import BulletinBoardDIModule
from simplebbs.domain.BulletinBoard.object.Poster import Poster
from simplebbs.domain.BulletinBoard.value.PosterId import PosterId
from simplebbs.domain.BulletinBoard.value.PosterName import PosterName
from simplebbs.domain.BulletinBoard.value.PosterPassword import PosterPassword


class PosterFactory:

    @staticmethod
    def create(id: str, name: str, password: str) -> Poster:

        injector = Injector([BulletinBoardDIModule()])
        poster = injector.get(Poster)
        poster.setValues(PosterId(id), PosterName(name), PosterPassword(password))

        return poster
