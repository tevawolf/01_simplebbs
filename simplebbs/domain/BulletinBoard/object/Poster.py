from typing import Union

from Crypto.Cipher import AES
from injector import inject

from simplebbs.domain.BulletinBoard.value.PosterId import PosterId
from simplebbs.domain.BulletinBoard.value.PosterName import PosterName
from simplebbs.domain.BulletinBoard.value.PosterPassword import PosterPassword
from simplebbs.infrastructure.repository.PosterRepository import PosterRepository


class Poster:
    """
    @DomainObject 投稿者
    @EntityObject （一意性のある）投稿者を表す
    """

    KEY = b'tevawolf20210701'

    @inject
    def __init__(self, r: PosterRepository):
        self.repository = r
        self.posterId = None
        self.posterName = None
        self.password = None

    def setValues(self, id: PosterId, name: PosterName, pswd: PosterPassword):
        self.posterId = id
        self.posterName = name
        self.password = pswd

    def createPoster(self) -> None:
        """
        投稿者を作成
        :return: なし
        """

        # パスワードの暗号化
        cipher = AES.new(self.KEY, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(self.password.getValue().encode('utf-8'))

        # 永続化
        self.repository.addPoster(
            self.posterId.getValue(),
            self.posterName.getValue(),
            ciphertext,
            tag,
            cipher.nonce
        )

    def authenticatePoster(self) -> Union[bool, str]:
        """
        投稿者の認証
        :return:認証の成否
        """
        poster = self.repository.getPoster(self.posterId.getValue())

        # 暗号化されたパスワードをKEYで複合し、入力されたパスワード文字列と一致するかチェック
        if poster:
            password = poster[2].tobytes()
            tag = poster[3].tobytes()
            nonce = poster[4].tobytes()

            cipher_dec = AES.new(self.KEY, AES.MODE_EAX, nonce)
            dec_password = cipher_dec.decrypt_and_verify(password, tag)

            return dec_password.decode('utf-8') == self.password.getValue(), poster[1]

        # IDが存在しない場合
        return False, ''
