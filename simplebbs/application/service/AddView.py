import datetime

from flask import redirect, request, url_for, session, flash
from flask.views import MethodView

from simplebbs.domain.BulletinBoard.service.BulletinBoardService import BulletinBoardService


class AddView(MethodView):

    @staticmethod
    def post():

        if session.__len__() != 0:
            BulletinBoardService.postBulletin(
                session['poster_name'], datetime.datetime.now(), request.form['title'], request.form['text'])
        else:
            BulletinBoardService.postBulletin(
                'ななしさん', datetime.datetime.now(), request.form['title'], request.form['text'])

        flash('掲示板に投稿しました。')

        return redirect(url_for('init'))
