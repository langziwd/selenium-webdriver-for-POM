'''
专通下水道
@project:Ecshop
@time:2018/4/28 19:38
@Author:langziwd
'''
from selenium.webdriver.common.by import By

from auto_driver.auto_driver import AutoDriver
from page.base_page import BasePage


# 创建登录子页面
class SubLoginPage(BasePage):
    def __init__(self,s:AutoDriver):
        super().__init__(s)

    def login(self):
        # 智能等待
        self.b.wait((By.ID,'loginButton'))
        # 点击登录
        self.b.f_element('id','loginButton').click()
        # 弹窗确认处理
        self.b.alert_accept()
