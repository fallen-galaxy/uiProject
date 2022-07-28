import page
from base.base_web import BaseWeb


class PageMisLogin(BaseWeb):

    def page_input_username(self, username):
        self.base_input_text(page.mis_username, username)

    def page_input_password(self, password):
        self.base_input_text(page.mis_password, password)

    def page_click_login_btn(self):
        js = "document.getElementById('inp1').disabled=false"
        self.driver.execute_script(js)
        self.base_click_element(page.mis_login_btn)

    def page_get_nickname(self):
        return self.base_get_text(page.mis_nickname)

    def page_mis_login(self, username, password):
        page.log.info("正在调用管理后台登录业务方法")
        self.page_input_username(username)
        self.page_input_password(password)
        self.page_click_login_btn()

    def page_mis_login_success(self, username='testid', password='testpwd123'):
        page.log.info("正在调用管理后台登录成功业务方法")
        self.page_input_username(username)
        self.page_input_password(password)
        self.page_click_login_btn()
