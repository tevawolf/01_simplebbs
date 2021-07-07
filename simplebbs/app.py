from flask import Flask

from simplebbs.application.view.AddView import AddView
from simplebbs.application.view.InitView import InitView
from simplebbs.application.view.SignInView import SignInView
from simplebbs.application.view.SignOutView import SignOutView
from simplebbs.application.view.SignUpView import SignUpView
from simplebbs.application.view.ThreadCreateView import ThreadCreateView
from simplebbs.application.view.ThreadView import ThreadView


def create_app():

    app = Flask(__name__, static_folder="presentation/static", template_folder="presentation/templates")
    app.config.from_object('simplebbs.config.Config')

    app.add_url_rule('/bbs/', view_func=InitView.as_view('init'))
    app.add_url_rule('/bbs/add/', view_func=ThreadCreateView.as_view('create_thread'))
    app.add_url_rule('/bbs/thread/<int:no>/<name>/', view_func=ThreadView.as_view('thread'))
    app.add_url_rule('/bbs/thread/add/', view_func=AddView.as_view('bulletin_add'))
    app.add_url_rule('/bbs/signin/', view_func=SignInView.as_view('signin'))
    app.add_url_rule('/bbs/signout/', view_func=SignOutView.as_view('signout'))
    app.add_url_rule('/bbs/signup/', view_func=SignUpView.as_view('signup'))

    return app


app = create_app()
