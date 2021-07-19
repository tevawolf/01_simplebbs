from flask import url_for, request, session, flash
from flask.views import MethodView
from werkzeug.utils import redirect

from simplebbs.domain.BulletinBoard.service.PosterService import PosterService


class SignInView(MethodView):
    """
    サインインView
    """

    @staticmethod
    def post():

        auth, poster_name = PosterService.signIn(
            request.form['signInId'], request.form['signInPassword']
        )
        if auth:
            session['poster_id'] = request.form['signInId']
            session['poster_name'] = poster_name
            flash('ユーザ{0}でサインインしました。'.format(request.form['signInId']))
        else:
            flash('サインインできませんでした。')

        return redirect(url_for('init'))
