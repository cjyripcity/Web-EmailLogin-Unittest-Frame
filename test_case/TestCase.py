import json
import unittest

from parameterized import parameterized

from business_stream.email_login import Login


def build_data():                    # json文件中读取测试数据
    with open('../test_data/login_data.json', encoding='utf-8') as f:
        result = json.load(f)        # json.load解码json文件对象  json.loads解码json字符串对象
        res = []
        for i in result:
            res.append((i.get('email'), i.get('password'), i.get('expect')))

    return res


class TestLogin(unittest.TestCase):
    #  方法级别夹具
    # def setUp(self):
    #     pass
    #
    # def tearDown(self):
    #     pass

    @parameterized.expand(build_data())  # 测试数据传参 （装饰器@）  为以下test_login测试用例的传入参数
    def test_login(self, email, password, expect):
        self.assertEqual(Login(email, password), expect)

