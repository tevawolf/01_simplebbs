from flask import url_for, request, session, flash
from flask.views import MethodView
from werkzeug.utils import redirect


class SignOutView(MethodView):

    @staticmethod
    def get():

        session.pop('poster_id', None)
        session.pop('poster_name', None)

        flash('サインアウトしました。')

        return redirect(url_for('init'))