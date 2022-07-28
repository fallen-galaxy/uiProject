from time import sleep

import pytest

import case
import page
from page.page_in import PageIn
from tool.get_driver import GetDriver
from tool.read_yaml import read_yaml


class TestMpArticle:

    def setup_class(self):
        case.log.info("类之前调用")
        # 获取驱动
        driver = GetDriver.get_web_driver(page.mp_url)
        # 获取统一入口类实例
        self.page_in = PageIn(driver)
        # 获取登录实例
        self.page_mp_login = self.page_in.page_get_page_mp_login()
        # 调用登录成功业务
        self.page_mp_login.page_mp_login_success()
        # 获取发布文章实例
        self.page_mp_article = self.page_in.page_get_page_mp_article()

    def teardown_class(self):
        case.log.info("类之后调用")
        # 关闭驱动
        GetDriver.quit_web_driver()

    @pytest.mark.parametrize("title,content,expect,channel", read_yaml("mp_article.yaml"))
    def test_mp_article(self, title, content, expect, channel):
        self.page_mp_article.page_mp_article(title, content)
        sleep(1)
        try:
            assert expect == self.page_mp_article.page_get_info()
        except Exception as e:
            case.log.error("断言出错：{}".format(e))
            self.page_mp_article.base_get_img()
            raise
