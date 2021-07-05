from flask import url_for, request, session, flash
from flask.views import MethodView
from werkzeug.utils import redirect

from simplebbs.domain.BulletinBoard.service.PosterService import PosterService


class SignInView(MethodView):

    @staticmethod
    def post():

        auth, posterName = PosterService.signIn(
            request.form['signInId'], request.form['signInPassword']
        )
        if auth:
            session['poster_id'] = request.form['signInId']
            session['poster_name'] = posterName
            flash('ユーザ{0}でサインインしました。'.format(request.form['signInId']))
        else:
            flash('サインインできませんでした。')

        return redirect(url_for('init'))