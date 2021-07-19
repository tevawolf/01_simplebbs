from flask import render_template, request, session, flash, url_for
from flask.views import MethodView
from werkzeug.utils import redirect

from simplebbs.domain.BulletinBoard.object.BulletinBoardThreadPublicLevel import BulletinBoardThreadPublicLevel
from simplebbs.domain.BulletinBoard.service.BulletinBoardThreadService import BulletinBoardThreadService


class ThreadReadonlyPasswordInputView(MethodView):

    @staticmethod
    def post():

        no = int(request.form['thread_no'])

        if BulletinBoardThreadService.authenticatePassword(no, request.form['thread_password']):
            session['thread_auth'] = True
            session['thread_auth_no'] = no
            flash('認証成功。スレッドに投稿できるようになりました。')
        else:
            flash('認証失敗。パスワードが違います。')

        return redirect(url_for('thread', no=no))
