import datetime

from flask import redirect, request, url_for, session, flash
from flask.views import MethodView

from simplebbs.domain.BulletinBoard.service.BulletinBoardThreadService import BulletinBoardThreadService


class AddView(MethodView):

    @staticmethod
    def post():

        thread_no = int(request.form['thread_no'])
        thread_name = request.form['thread_name']

        if session.__len__() != 0:
            BulletinBoardThreadService.postBulletin(
                session['poster_name'], datetime.datetime.now(), request.form['title'], request.form['text'], thread_no)
        else:
            BulletinBoardThreadService.postBulletin(
                'ななしさん', datetime.datetime.now(), request.form['title'], request.form['text'], thread_no)

        flash('スレッドに投稿しました。')

        return redirect(url_for('thread', no=thread_no, name=thread_name))
