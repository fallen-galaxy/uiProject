import pytest

import case
from page.page_in import PageIn
from tool.get_driver import GetDriver
from tool.read_yaml import read_yaml


class TestAppLogin:

    def setup_class(self):
        case.log.info("类之前调用")
        # 获取驱动
        driver = GetDriver.get_app_driver()
        # 获取统一入口类实例
        self.page_in = PageIn(driver)
        # 获取登录实例
        self.page_app_login = self.page_in.page_get_page_app_login()

    def teardown_class(self):
        case.log.info("类之后调用")
        # 关闭驱动
        GetDriver.quit_app_driver()

    @pytest.mark.parametrize("phonenum,authcode", read_yaml('app_login.yaml'))
    def test_app_login(self, phonenum, authcode):
        self.page_app_login.page_app_login(phonenum, authcode)
        try:
            assert self.page_app_login.page_is_login_success()
        except Exception as e:
            case.log.error("断言出错：{}".format(e))
            self.page_app_login.base_get_img()
            raise
