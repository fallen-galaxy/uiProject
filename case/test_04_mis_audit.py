import page
import case
from page.page_in import PageIn
from tool.get_driver import GetDriver


class TestMisAudit:

    def setup_class(self):
        case.log.info("类之前调用")
        # 获取驱动
        driver = GetDriver.get_web_driver(page.mis_url)
        # 获取统一入口类实例
        self.page_in = PageIn(driver)
        # 获取登录实例
        self.page_mis_login = self.page_in.page_get_page_mis_login()
        # 调用登录成功业务
        self.page_mis_login.page_mis_login_success()
        # 获取审核文章实例
        self.page_mis_audit = self.page_in.page_get_page_mis_audit()

    def teardown_class(self):
        case.log.info("类之后调用")
        # 关闭驱动
        GetDriver.quit_web_driver()

    def test_mis_audit(self):
        self.page_mis_audit.page_mis_audit(page.title, page.channel)
        try:
            assert self.page_mis_audit.page_assert_audit()
        except Exception as e:
            case.log.error("断言出错：{}".format(e))
            self.page_mis_audit.base_get_img()
            raise
