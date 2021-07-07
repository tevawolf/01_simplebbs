import datetime

from flask import redirect, request, url_for, flash
from flask.views import MethodView

from simplebbs.domain import BulletinBoardService


class ThreadCreateView(MethodView):

    @staticmethod
    def post():

        BulletinBoardService.createThread(request.form['title'])

        flash('スレッドを作成しました。')

        return redirect(url_for('init'))
