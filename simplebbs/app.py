from flask import Flask
from jinja2 import FileSystemLoader

from simplebbs.application.service.AddView import AddView
from simplebbs.application.service.InitView import InitView


def create_app():

    # app = Flask(__name__, static_folder="presentation/static")
    app = Flask(__name__, static_folder="presentation/static", template_folder="presentation/templates")
    # app.jinja_loader = FileSystemLoader('simplebbs/presentation/templates')
    app.config.from_object('simplebbs.config.Config')

    app.add_url_rule('/bbs/', view_func=InitView.as_view('init'))
    app.add_url_rule('/bbs/add/', view_func=AddView.as_view('add'))

    return app


app = create_app()
