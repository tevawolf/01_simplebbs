from injector import Injector

from simplebbs.binds import BulletinBoardDIModule
from simplebbs.domain.BulletinBoard.object import Bulletin
from simplebbs.domain.BulletinBoard.object.BulletinBoardThread import BulletinBoardThread
from simplebbs.domain.BulletinBoard.object.BulletinBoardThreadPublicLevel import BulletinBoardThreadPublicLevel
from simplebbs.domain.BulletinBoard.value.ThreadName import ThreadName
from simplebbs.domain.BulletinBoard.value.ThreadNo import ThreadNo
from simplebbs.domain.BulletinBoard.value.ThreadPassword import ThreadPassword


class BulletinBoardThreadFactory:

    @staticmethod
    def create(no: int, name: str, level: int, password: str) -> Bulletin:

        injector = Injector([BulletinBoardDIModule()])
        thread = injector.get(BulletinBoardThread)
        thread.setValues(ThreadNo(no), ThreadName(name), BulletinBoardThreadPublicLevel(level), ThreadPassword(password))

        return thread
