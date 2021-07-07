from flask import render_template
from flask.views import MethodView

from simplebbs.domain.BulletinBoard.service.BulletinBoardService import BulletinBoardService


class InitView(MethodView):

    @staticmethod
    def get():
        bulletin_board = BulletinBoardService.initDisplay()

        # JSONシリアライズできないクラスはセッション保持不可能・・・
        # bulletinBoardをセッション保持する
        # session['bulletinBoard'] = bulletin_board

        return render_template('bulletinBoard.html', bulletin_board=bulletin_board.postAllThreads())
