from time import sleep

from selenium.webdriver.common.by import By

import base
from base.base import Base


class BaseWeb(Base):

    # 下拉框选择
    def base_web_click_element(self, placeholder_text, click_text):
        base.log.info("下拉框选择")
        loc = By.CSS_SELECTOR, '[placeholder="{}"]'.format(placeholder_text)
        self.base_click_element(loc)
        sleep(1)
        loc = By.XPATH, "//*[text()='{}']".format(click_text)
        self.base_click_element(loc)

    # 判断元素是否存在
    def base_web_is_exist(self, text):
        base.log.info("查看文本是否存在")
        loc = By.XPATH, "//*[text()='{}']".format(text)
        try:
            self.base_find_element(loc, timeout=3)
            return True
        except:
            return False
