from flask import render_template
from flask.views import MethodView

from simplebbs.domain.BulletinBoard.object.BulletinBoardThreadPublicLevel import BulletinBoardThreadPublicLevel
from simplebbs.domain.BulletinBoard.service.BulletinBoardService import BulletinBoardService


class InitView(MethodView):
    """
    初期表示View
    """

    @staticmethod
    def get():
        bulletin_board = BulletinBoardService.initDisplay()

        # JSONシリアライズできないクラスはセッション保持不可能・・・
        # bulletinBoardをセッション保持する
        # session['bulletinBoard'] = bulletin_board

        return render_template('bulletin_board.html',
                               bulletin_board=bulletin_board.postAllThreads(),
                               public_levels=(
                                   BulletinBoardThreadPublicLevel.公開,
                                   BulletinBoardThreadPublicLevel.閲覧のみ,
                                   BulletinBoardThreadPublicLevel.非公開,
                                   )
                               )
