import datetime

from flask import redirect, request, url_for
from flask.views import MethodView

from simplebbs.domain.BulletinBoard.service.BulletinBoardService import BulletinBoardService


class AddView(MethodView):

    @staticmethod
    def post():

        BulletinBoardService.postBulletin(
            request.form['title'], datetime.datetime.now(), request.form['text'])

        return redirect(url_for('init'))
