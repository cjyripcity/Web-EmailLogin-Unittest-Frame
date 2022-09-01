import unittest

from test_case import TestCase

# 1. 实例化（创建对象）套件对象
from test_case.TestCase import TestLogin

suite = unittest.TestSuite()

# 2. 使用套件对象添加用例方法
# 方式1，套件对象.addTest(测试类名('方法名'))
# suite.addTest(TestCase('test_login'))


# 方式2，将一个测试类中的所有方法添加
# 套件对象.addTest(unittest.makeSuite(测试类名))
suite.addTest(unittest.makeSuite(TestLogin))


# 实例化运行对象
runner = unittest.TextTestRunner()
# 5. 使用运行对象去执行套件对象
runner.run(suite)