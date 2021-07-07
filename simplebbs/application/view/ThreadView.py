from flask import render_template, request
from flask.views import MethodView

from simplebbs.domain.BulletinBoard.service.BulletinBoardThreadService import BulletinBoardThreadService


class ThreadView(MethodView):

    @staticmethod
    def get(no: int, name: str):

        thread = BulletinBoardThreadService.displayThread(no, name)

        return render_template('thread.html', thread=thread)
