
import pytest

from page.page_in import PageIn
from tool.get_driver import GetDriver
import page
import case
from tool.read_yaml import read_yaml


class TestMpLogin:

    def setup_class(self):
        case.log.info("类之前调用")
        # 获取驱动
        driver = GetDriver.get_web_driver(page.mp_url)
        # 获取统一入口类实例
        self.page_in = PageIn(driver)
        # 获取登录实例
        self.page_mp_login = self.page_in.page_get_page_mp_login()

    def teardown_class(self):
        case.log.info("类之后调用")
        # 关闭驱动
        GetDriver.quit_web_driver()

    @pytest.mark.parametrize("username,authcode,expect", read_yaml("mp_login.yaml"))
    def test_mp_login(self, username, authcode, expect):
        self.page_mp_login.page_mp_login(username, authcode)
        try:
            assert expect == self.page_mp_login.page_get_nickname()
        except Exception as e:
            case.log.error("断言出错：{}".format(e))
            self.page_mp_login.base_get_img()
            raise
