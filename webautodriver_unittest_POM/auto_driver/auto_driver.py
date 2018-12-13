'''
专通下水道
@project:Ecshop
@time:2018/4/28 19:31
@Author:langziwd
'''
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#封装
class AutoDriver(object):
    # 构建属性
    def __init__(self):
        self.a = webdriver.Firefox()
        self.base_url = 'http://www.cgbchina.com.cn/'

    # 窗口最大化
    def max_window(self):
        self.a.maximize_window()

    # 退出
    def quit_bro(self):
        self.a.quit()

    # 打开网址
    def go_url(self,url):
        self.a.get(self.base_url+url)

    # 定位
    def f_element(self, by, selector):
        if by == 'id':
            return self.a.find_element_by_id(selector)
        elif by == 'xpa':
            return self.a.find_element_by_xpath(selector)
        elif by == 'ltext':
            return self.a.find_element_by_link_text(selector)
    # 跳转到新窗口
    def switch_newindow(self):
        all_windows = self.a.window_handles
        self.a.switch_to.window(all_windows[-1])

    # 弹窗确认处理
    def alert_accept(self):
        a=self.a.switch_to.alert
        a.accept()

    # 设置显示等待
    def wait(self,locator):
        WebDriverWait(self.a, 5, 0.5).until(expected_conditions.presence_of_element_located(locator))

    # # 悬浮
    def ActionChains(self, element):
        ActionChains(self.a).move_to_element(element).perform()

    # 跳进表单
    def switch_frame(self, frame_reference):
        self.a.switch_to.frame(frame_reference)

    # 跳出表单
    def switch_out_all_frame(self):
        self.a.switch_to.default_content()

    # 构建驱动
    def open_onelines(self,path):
        file = open(path,mode='r',encoding='utf8')
        msg = csv.reader(file,dialect='excel')
        a=1
        b=0
        result = {}
        for i in msg:
            result1 = {a:i[b]}
            result.update(result1)
            a+=1
            b+=1
        return result