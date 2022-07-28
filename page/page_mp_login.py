from time import sleep

import page
from base.base_web import BaseWeb


class PageMpLogin(BaseWeb):

    # 输入用户名
    def page_input_username(self, username):
        self.base_input_text(page.mp_username, username)

    # 输入验证码
    def page_input_authcode(self, authcode):
        self.base_input_text(page.mp_authcode, authcode)

    # 点击登录按钮
    def page_click_login_btn(self):
        self.base_click_element(page.mp_login_btn)
        sleep(3)

    # 获取昵称
    def page_get_nickname(self):
        return self.base_get_text(page.mp_nickname)

    # 组合业务 --> 登录测试
    def page_mp_login(self, username, authcode):
        page.log.info("正在调用媒体前台登录业务方法 {} {}".format(username, authcode))
        self.page_input_username(username)
        self.page_input_authcode(authcode)
        self.page_click_login_btn()

    # 组合业务 --> 登录成功
    def page_mp_login_success(self, username="13911111111", authcode="246810"):
        page.log.info("正在调用媒体前台登录成功业务方法 {} {}".format(username, authcode))
        self.page_input_username(username)
        self.page_input_authcode(authcode)
        self.page_click_login_btn()
