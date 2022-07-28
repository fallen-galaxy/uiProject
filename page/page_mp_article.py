import page
from base.base_web import BaseWeb


class PageMpArticle(BaseWeb):

    # 点击 内容管理
    def page_click_content_manage(self):
        self.base_click_element(page.mp_content_manage)

    # 点击 发布文章
    def page_click_publish_article(self):
        self.base_click_element(page.mp_publish_article)

    # 输入 标题信息
    def page_input_title(self, title):
        self.base_input_text(page.mp_title, title)

    # 输入 内容信息
    def page_input_content(self, content):
        iframe = self.base_find_element(page.mp_iframe)
        self.driver.switch_to.frame(iframe)
        self.base_input_text(page.mp_content, content)
        self.driver.switch_to.default_content()

    # 点击 封面信息
    def page_click_cover(self):
        self.base_click_element(page.mp_cover)

    # 点击 频道信息
    def page_click_channel(self):
        self.base_web_click_element("请选择", page.channel)

    # 点击 发表按钮
    def page_click_submit(self):
        self.base_click_element(page.mp_submit)

    # 获取 提示信息
    def page_get_info(self):
        return self.base_get_text(page.mp_result)

    # 组合业务 --> 发布文章
    def page_mp_article(self, title, content):
        page.log.info("正在调用媒体前台发布文章业务方法")
        self.page_click_content_manage()
        self.page_click_publish_article()
        self.page_input_title(title)
        self.page_input_content(content)
        self.page_click_cover()
        self.page_click_channel()
        self.page_click_submit()
