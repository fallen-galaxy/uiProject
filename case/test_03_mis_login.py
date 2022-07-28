import pytest

import case
import page
from page.page_in import PageIn
from tool.get_driver import GetDriver
from tool.read_yaml import read_yaml


class TestMisLogin:

    def setup_class(self):
        case.log.info("类之前调用")
        # 获取驱动
        driver = GetDriver.get_web_driver(page.mis_url)
        # 获取统一入口类实例
        self.page_in = PageIn(driver)
        # 获取登录实例
        self.page_mis_login = self.page_in.page_get_page_mis_login()

    def teardown_class(self):
        case.log.info("类之后调用")
        # 关闭驱动
        GetDriver.quit_web_driver()

    @pytest.mark.parametrize("username,password,expect", read_yaml("mis_login.yaml"))
    def test_mis_login(self, username, password, expect):
        self.page_mis_login.page_mis_login(username, password)
        try:
            assert expect in self.page_mis_login.page_get_nickname()
        except Exception as e:
            case.log.error("断言出错：{}".format(e))
            self.page_mis_login.base_get_img()
            raise
