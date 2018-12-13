'''
专通下水道
@project:Ecshop
@time:2018/4/28 19:58
@Author:langziwd
'''
from selenium.webdriver.common.by import By

from auto_driver.auto_driver import AutoDriver



# 创建登录成功后的主页面
class BasePage002(object):
    def __init__(self,b:AutoDriver):
         self.b = b

    def next(self):
        # 智能等待
        self.b.wait((By.ID,'buttonNextDiv'))
        # 点击下一步
        n =self.b.f_element('id','buttonNextDiv')
        n.click()
        n.click()
        n.click()
        n.click()
        n.click()
        n.click()

    def charge_click(self):
        # 点击转账汇款
        self.b.f_element('ltext','转账汇款').click()

        # 悬浮至跨行资金归集
        self.b.wait((By.LINK_TEXT,'跨行资金归集'))
        element = self.b.f_element('ltext','跨行资金归集')
        self.b.ActionChains(element)
        # 点击主动资金归集
        self.b.wait((By.LINK_TEXT,'主动资金归集'))
        self.b.f_element('ltext','主动资金归集').click()

