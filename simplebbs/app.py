from flask import Flask

from simplebbs.application.service.AddView import AddView
from simplebbs.application.service.InitView import InitView
from simplebbs.application.service.SignInView import SignInView
from simplebbs.application.service.SignOutView import SignOutView
from simplebbs.application.service.SignUpView import SignUpView


def create_app():

    app = Flask(__name__, static_folder="presentation/static", template_folder="presentation/templates")
    app.config.from_object('simplebbs.config.Config')

    app.add_url_rule('/bbs/', view_func=InitView.as_view('init'))
    app.add_url_rule('/bbs/add/', view_func=AddView.as_view('add'))
    app.add_url_rule('/bbs/signin/', view_func=SignInView.as_view('signin'))
    app.add_url_rule('/bbs/signout/', view_func=SignOutView.as_view('signout'))
    app.add_url_rule('/bbs/signup/', view_func=SignUpView.as_view('signup'))

    return app


app = create_app()
