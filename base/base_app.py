from time import sleep

from selenium.webdriver.common.by import By

import base
from base.base import Base


class BaseApp(Base):

    # 判断元素是否存在
    def base_app_is_exist(self, loc):
        base.log.info("查看文本是否存在")
        try:
            self.base_find_element(loc, timeout=3)
            return True
        except:
            return False

    # 右左滑动屏幕
    def base_app_right_slide_left(self, loc_area, click_text):
        base.log.info("正在调用从右向左滑动")
        el = self.base_find_element(loc_area)
        y = el.location.get("y")
        width = el.size.get("width")
        height = el.size.get("height")
        start_x = width * 0.8
        start_y = y + height * 0.5
        end_x = width * 0.2
        end_y = y + height * 0.5
        loc = By.XPATH, "//android.widget.HorizontalScrollView/*[contains(@text,'{}')]".format(click_text)
        while True:
            page_source = self.driver.page_source
            try:
                el = self.base_find_element(loc, timeout=3)
                el.click()
                break
            except:
                self.driver.swipe(start_x, start_y, end_x, end_y, duration=2000)
            if page_source == self.driver.page_source:
                raise

    # 下上滑动屏幕
    def base_app_down_slide_up(self, loc_area, click_text):
        base.log.info("正在调用从下向上滑动")
        el = self.base_find_element(loc_area)
        width = el.size.get("width")
        height = el.size.get("height")
        start_x = width * 0.5
        start_y = height * 0.8
        end_x = width * 0.5
        end_y = height * 0.2
        loc = By.XPATH, "//*[@bounds='[0,520][1440,2288]']/*[contains(@text,'{}')]".format(click_text)
        while True:
            page_source = self.driver.page_source
            try:
                sleep(2)
                el = self.base_find_element(loc, timeout=3)
                sleep(2)
                el.click()
                break
            except:
                self.driver.swipe(start_x, start_y, end_x, end_y, duration=2000)
            if page_source == self.driver.page_source:
                raise

