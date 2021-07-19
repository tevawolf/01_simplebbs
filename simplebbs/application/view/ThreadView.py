from flask import render_template, request
from flask.views import MethodView

from simplebbs.domain.BulletinBoard.object.BulletinBoardThreadPublicLevel import BulletinBoardThreadPublicLevel
from simplebbs.domain.BulletinBoard.service.BulletinBoardThreadService import BulletinBoardThreadService


class ThreadView(MethodView):

    @staticmethod
    def get(no: int):
        thread = BulletinBoardThreadService.displayThread(no)

        return render_template('thread.html', thread=thread, PUBLIC_LEVEL_READONLY=BulletinBoardThreadPublicLevel.閲覧のみ)
