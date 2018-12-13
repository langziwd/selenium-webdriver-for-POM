import unittest
# 测试套件
from test_case import test_case_001_login
from test_case.test_case_001_login import TestCase001Login


if __name__=='__main__':
    # 构造测试集
    suite=unittest.TestSuite()
    # 添加测试用例（类名+测试方法名）
    # suite.addTest(TestCase001Login('test_login'))
    suite.addTest(unittest.makeSuite(test_case_001_login.TestCase001Login))

    # 运行测试集合
    runner=unittest.TextTestRunner()
    runner.run(suite)