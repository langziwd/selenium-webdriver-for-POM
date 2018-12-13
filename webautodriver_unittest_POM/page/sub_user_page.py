import time
from selenium.webdriver.common.by import By

from auto_driver.auto_driver import AutoDriver
from page.base_page002 import BasePage002


# 创建登录后主动资金归集的子页面
class SubUserPage(BasePage002):
    def __init__(self,s:AutoDriver):
        super().__init__(s)

    # 录入信息
    def insert_msg(self,payAmount):
        # 智能等待
        self.b.wait((By.XPATH,'/html/body/div[6]/div[2]/div[2]/div/div/table[2]/tbody/tr/td/div/iframe'))
        # 跳进表单
        self.b.switch_frame(self.b.f_element('xpa','/html/body/div[6]/div[2]/div[2]/div/div/table[2]/tbody/tr/td/div/iframe'))
        self.b.wait((By.ID,'0075557272277119601BG'))
        # 定位支付卡点击
        self.b.f_element('id','0075557272277119601BG').click()
        # 输入支付金额
        a = self.b.f_element('id','payAmount')
        a.clear()
        a.send_keys(payAmount)
        # 点击下一步
        self.b.f_element('id','buttonNext').click()
        # 跳出表单
        self.b.switch_out_all_frame()

    # 确认交易
    def confirm_deal(self,checkCode,securitySmsCode):

        # 智能等待
        self.b.wait((By.XPATH,'//iframe[contains(@src,"html/transfer/b100101_transferPageConfirm.htm")]'))
        # 进入表单
        self.b.switch_frame(self.b.f_element('xpa','//iframe[contains(@src,"html/transfer/b100101_transferPageConfirm.htm")]'))
        # 智能等待
        self.b.wait((By.ID,'checkCode'))
        # 输入验证码
        a1 = self.b.f_element('id','checkCode')
        a1.clear()
        a1.send_keys(checkCode)
        # 点击获取验证码
        self.b.wait((By.ID,'smsA'))
        self.b.f_element('id','smsA').click()
        # 输入验证码
        a2 = self.b.f_element('id','securitySmsCode')
        a2.clear()
        a2.send_keys(securitySmsCode)
        # 点击确认
        self.b.f_element('id','buttonNext').click()
        # 跳出表单
        self.b.switch_out_all_frame()

    # 定义确认更新操作
    def confirm_update(self):
        # 智能等待
        self.b.wait((By.XPATH,'/html/body/div[26]/div/table[2]/tbody/tr/td/div/iframe'))
        # 跳进表单
        self.b.switch_frame(self.b.f_element('xpa','/html/body/div[26]/div/table[2]/tbody/tr/td/div/iframe'))
        # 弹窗确认
        self.b.wait((By.ID,'buttonNext'))
        self.b.f_element('id','buttonNext').click()
        # 跳出表单
        self.b.switch_out_all_frame()
        self.b.wait((By.XPATH,'/html/body/div[26]/div/table[2]/tbody/tr/td/div/iframe[1]'))
        # 跳进表单
        self.b.switch_frame(self.b.f_element('xpa','/html/body/div[26]/div/table[2]/tbody/tr/td/div/iframe[1]'))
        self.b.wait((By.XPATH,'/html/body/div/div[2]/a'))
        # 关闭弹窗
        self.b.f_element('xpa','/html/body/div/div[2]/a').click()