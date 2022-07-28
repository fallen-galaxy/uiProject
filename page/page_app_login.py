from base.base_app import BaseApp
import page


class PageAppLogin(BaseApp):

    def page_input_phonenum(self, phonenum):
        self.base_input_text(page.app_phonenum, phonenum)

    def page_input_authcode(self, authcode):
        self.base_input_text(page.app_authcode, authcode)

    def page_click_login_btn(self):
        self.base_click_element(page.app_login_btn)

    def page_is_login_success(self):
        return self.base_app_is_exist(page.app_mine_unit)

    # 组合业务
    def page_app_login(self, phonenum, authcode):
        page.log.info("正在调用app登录业务")
        self.page_input_phonenum(phonenum)
        self.page_input_authcode(authcode)
        self.page_click_login_btn()

    # 组合业务
    def page_app_login_success(self, phonenum='13812345678', authcode='246810'):
        page.log.info("正在调用app登录成功业务")
        self.page_input_phonenum(phonenum)
        self.page_input_authcode(authcode)
        self.page_click_login_btn()
