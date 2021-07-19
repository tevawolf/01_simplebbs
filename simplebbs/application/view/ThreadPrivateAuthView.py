from flask import render_template, request, session, url_for
from flask.views import MethodView
from werkzeug.utils import redirect

from simplebbs.domain.BulletinBoard.object.BulletinBoardThreadPublicLevel import BulletinBoardThreadPublicLevel
from simplebbs.domain.BulletinBoard.service.BulletinBoardThreadService import BulletinBoardThreadService


class ThreadPrivateAuthView(MethodView):

    @staticmethod
    def get(no: int):
        if 'thread_auth' in session:
            if session['thread_auth'] and session['thread_auth_no'] == no:
                return redirect(url_for('thread', no=no))

        return render_template('thread_private_auth.html', no=no)

