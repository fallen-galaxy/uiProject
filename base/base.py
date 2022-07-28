from time import sleep

import allure
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait

import base


class Base:

    # 初始化
    def __init__(self, driver):
        """
        :param driver: 浏览器驱动
        """
        base.log.info("初始化驱动：{}".format(driver))
        self.driver = driver

    # 查找元素
    def base_find_element(self, loc, timeout=30, poll_frequency=0.5):
        """
        :param loc: 列表或元组
        :param timeout: 查找元素超时时间，30秒
        :param poll_frequency: 查找元素频率，0.5秒
        :return: 返回元素对象
        """
        base.log.info("正在查找元素：{}".format(loc))
        return (WebDriverWait(driver=self.driver,
                              timeout=timeout,
                              poll_frequency=poll_frequency)
                .until(method=lambda x: x.find_element(*loc)))

    # 点击元素
    def base_click_element(self, loc):
        """
        :param loc: 元素定位
        """
        el = self.base_find_element(loc)
        base.log.info("正在点击元素：{}".format(loc))
        sleep(1)
        el.click()
        sleep(1)

    # 输入文本
    def base_input_text(self, loc, value):
        """
        :param loc: 元素定位
        :param value: 文本内容
        """
        el = self.base_find_element(loc)
        base.log.info("正在输入文本：{} {}".format(loc, value))
        sleep(1)
        el.send_keys(Keys.CONTROL, 'a')
        sleep(1)
        el.send_keys(value)

    # 获取文本
    def base_get_text(self, loc):
        """
        :param loc: 元素定位
        :return: 返回文本
        """
        el = self.base_find_element(loc)
        base.log.info("正在获取文本：{} {}".format(loc, el.text))
        sleep(1)
        return el.text

    # 获取截图
    def base_get_img(self):
        """
        :return:
        """
        base.log.error("正在生成截图")
        self.driver.get_screenshot_as_file("./image/err.png")
        base.log.error("图片写入报告")
        self.__base_write_img()

    # 图片写入
    def __base_write_img(self):
        """
        :return:
        """
        with open("./image/err.png", "rb") as f:
            allure.attach("错误原因", f.read(), allure.attachment_type.PNG)
