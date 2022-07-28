import case
import page
from page.page_in import PageIn
from tool.get_driver import GetDriver


class TestAppArticle:

    def setup_class(self):
        case.log.info("类之前调用")
        # 获取驱动
        driver = GetDriver.get_app_driver()
        # 获取统一入口类实例
        self.page_in = PageIn(driver)
        # 获取登录实例
        self.page_app_login = self.page_in.page_get_page_app_login()
        # 调用登录成功业务
        self.page_app_login.page_app_login_success()
        # 获取查看文章实例
        self.page_app_article = self.page_in.page_get_page_app_article()

    def teardown_class(self):
        case.log.info("类之后调用")
        # 关闭驱动
        GetDriver.quit_app_driver()

    def test_app_article(self, channel=page.channel, title=page.title):
        try:
            self.page_app_article.page_app_article(channel, title)
        except Exception as e:
            case.log.error("断言出错：{}".format(e))
            self.page_app_article.base_get_img()
            raise

