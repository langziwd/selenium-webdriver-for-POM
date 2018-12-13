'''
专通下水道
@project:Ecshop
@time:2018/4/28 19:37
@Author:langziwd
'''
from selenium.webdriver.common.by import By

from auto_driver.auto_driver import AutoDriver

# 创建首页主页面类
class BasePage(object):
    def __init__(self,b:AutoDriver):
        self.b = b

    # 点击在线演示
    def show_online(self):
        # 智能等待
        self.b.wait((By.XPATH, '/html/body/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/ul/li[2]/a'))
        # 点击在线演示
        self.b.f_element('xpa','/html/body/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/ul/li[2]/a').click()
        # 窗口跳转
        self.b.switch_newindow()