from page.page_app_article import PageAppArticle
from page.page_app_login import PageAppLogin
from page.page_mis_audit import PageMisAudit
from page.page_mis_login import PageMisLogin
from page.page_mp_article import PageMpArticle
from page.page_mp_login import PageMpLogin


class PageIn:

    # driver
    def __init__(self, driver):
        self.driver = driver

    # page_mp_login
    def page_get_page_mp_login(self):
        return PageMpLogin(self.driver)

    # page_mp_article
    def page_get_page_mp_article(self):
        return PageMpArticle(self.driver)

    # page_mis_login
    def page_get_page_mis_login(self):
        return PageMisLogin(self.driver)

    # page_mis_audit
    def page_get_page_mis_audit(self):
        return PageMisAudit(self.driver)

    # page_app_login
    def page_get_page_app_login(self):
        return PageAppLogin(self.driver)

    # page_app_article
    def page_get_page_app_article(self):
        return PageAppArticle(self.driver)
