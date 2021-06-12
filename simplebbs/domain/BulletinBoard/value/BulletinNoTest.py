import unittest

from simplebbs.domain.BulletinBoard.value.BulletinNo import BulletinNo


class MyTestCase(unittest.TestCase):

    def test_min(self):
        try:
            no = BulletinNo(-1)
        except ValueError as e:
            print(e)
            self.assertEqual(
                True, True
            )
            return

        self.assertEqual(True, False)

    def test_minPlusOne(self):
        try:
            no = BulletinNo(0)
        except ValueError as e:
            print(e)
            self.assertEqual(
                True, False
            )
            return

        self.assertEqual(True, True)

    def test_maxMinusOne(self):
        try:
            no = BulletinNo(100000)
        except ValueError as e:
            print(e)
            self.assertEqual(
                True, False
            )
            return

        self.assertEqual(True, True)

    def test_max(self):
        try:
            no = BulletinNo(100001)
        except ValueError as e:
            print(e)
            self.assertEqual(
                True, True
            )
            return

        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
