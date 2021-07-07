from injector import Injector

from simplebbs.binds import BulletinBoardDIModule
from simplebbs.domain.BulletinBoard.object import Bulletin
from simplebbs.domain.BulletinBoard.object.BulletinBoardThread import BulletinBoardThread
from simplebbs.domain.BulletinBoard.value.ThreadName import ThreadName
from simplebbs.domain.BulletinBoard.value.ThreadNo import ThreadNo


class BulletinBoardThreadFactory:

    @staticmethod
    def create(no: int, name: str) -> Bulletin:

        injector = Injector([BulletinBoardDIModule()])
        thread = injector.get(BulletinBoardThread)
        thread.setValues(ThreadNo(no), ThreadName(name))

        return thread
