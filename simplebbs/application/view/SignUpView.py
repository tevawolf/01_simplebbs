from flask import request, url_for, session, flash
from flask.views import MethodView
from werkzeug.utils import redirect

from simplebbs.domain.BulletinBoard.service.PosterService import PosterService


class SignUpView(MethodView):
    """
    サインアップView
    """

    @staticmethod
    def post():

        PosterService.signUp(
            request.form['posterId'], request.form['posterName'], request.form['posterPassword']
        )

        # サインインも同時に行う
        session['poster_id'] = request.form['posterId']
        session['poster_name'] = request.form['posterName']

        flash('ユーザ{0}：{1}でサインアップしました。'.format(request.form['posterId'], request.form['posterName']))

        return redirect(url_for('init'))
