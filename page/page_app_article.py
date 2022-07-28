from base.base_app import BaseApp
import page


class PageAppArticle(BaseApp):

    def page_click_channel(self, click_text):
        self.base_app_right_slide_left(page.app_channel_area, click_text)

    def page_click_article(self, click_text):
        self.base_app_down_slide_up(page.app_article_ares, click_text)

    def page_app_article(self, channel, title):
        page.log.info("正在调用用户前台查看文章业务方法")
        self.page_click_channel(channel)
        self.page_click_article(title)
