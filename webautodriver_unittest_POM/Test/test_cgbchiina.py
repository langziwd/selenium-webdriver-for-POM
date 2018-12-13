'''
专通下水道
@project:Ecshop
@time:2018/4/28 19:29
@Author:langziwd
'''
# 6.通过自动化实现以下功能：-----用封装、POM、数据驱动实现
#   打开URLhttp://www.cgbchina.com.cn/-----1点击在线演示-----2点击立即登录-----3点击（6个下一步）
#   -----4点击转账汇款----5点击跨行资金归集-----6主动资金归集-----7选择支付卡和支付金额-----
#   8确认归集信息----9确认更新
import csv
import unittest
from auto_driver.auto_driver import AutoDriver
# from page.sub_login_page import SubLoginPage
# from page.sub_user_page import SubUserPage

# 创建广发ui测试框架
class TestCgbcChina(unittest.TestCase):
    def setUp(self):
        # 导入封装
        self.d = AutoDriver()
        # 导入登录子页面
        self.s1 = SubLoginPage(self.d)
        # 导入主动资金归集子页面
        self.s2 = SubUserPage(self.d)
        # 窗口最大化
        self.d.max_window()
    def tearDown(self):
        # 退出浏览器
        self.d.quit_bro()
    def test_cgbc(self):
        '''主动资金归集测试'''
        # 打开网址
        self.d.go_url('')

        # # 点击在线演示
        self.s1.show_online()

        # # 点击登录
        self.s1.login()

        # # 点击下一步
        self.s2.next()

        # # 点击转账汇款---跨行资金归集---主动资金归集
        self.s2.charge_click()

        # 录入信息---数据驱动

        insert_msg_data = open(r'C:\Users\THINK\PycharmProjects\TestProject\data\insert_msg_data.csv',mode='r',encoding='utf8')
        insert_r = csv.reader(insert_msg_data)
        for i in insert_r:
            dict_insert={
                'Amount':i[0]
            }

            self.s2.insert_msg(dict_insert['Amount'])

        # 确认交易---数据驱动

        confirm_deal_data = open(r'C:\Users\THINK\PycharmProjects\TestProject\data\confirm_deal_data',mode='r',encoding='utf8')
        confirm_deal_r = csv.reader(confirm_deal_data)
        for j in confirm_deal_r:
            dict_confirm_deal={
                    'checkCode':j[0],
                    'securitySmsCode':j[1]
            }
            self.s2.confirm_deal(dict_confirm_deal['checkCode'],dict_confirm_deal['securitySmsCode'])

        # 确认更新操作
        self.s2.confirm_update()
