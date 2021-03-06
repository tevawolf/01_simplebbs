from datetime import datetime

from injector import Injector

from simplebbs.binds import BulletinBoardDIModule
from simplebbs.domain.BulletinBoard.object import Bulletin
from simplebbs.domain.BulletinBoard.value.BulletinNo import BulletinNo
from simplebbs.domain.BulletinBoard.value.PostTitle import PostTitle
from simplebbs.domain.BulletinBoard.value.PosterName import PosterName
from simplebbs.domain.BulletinBoard.value.PostDateTime import PostDateTime
from simplebbs.domain.BulletinBoard.value.PostText import PostText
from simplebbs.domain.BulletinBoard.value.ThreadNo import ThreadNo


class BulletinFactory:

    @staticmethod
    def create(no: int, name: str, dt: datetime, title: str, text: str, thread_no: int) -> Bulletin:

        injector = Injector([BulletinBoardDIModule()])
        bulletin = injector.get(Bulletin)
        bulletin.setValues(
            BulletinNo(no), PosterName(name), PostDateTime(dt), PostTitle(title), PostText(text), ThreadNo(thread_no)
        )

        return bulletin
