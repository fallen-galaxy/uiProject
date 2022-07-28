from selenium import webdriver

import appium.webdriver

import page
import tool


class GetDriver:
    __web_driver = None
    __app_driver = None

    @classmethod
    def get_web_driver(cls, url):
        tool.log.info("get_web_driver")
        if cls.__web_driver is None:
            cls.__web_driver = webdriver.Chrome()
            cls.__web_driver.maximize_window()
            cls.__web_driver.get(url)
        return cls.__web_driver

    @classmethod
    def quit_web_driver(cls):
        tool.log.info("quit_web_driver")
        if cls.__web_driver is not None:
            cls.__web_driver.quit()
            cls.__web_driver = None

    @classmethod
    def get_app_driver(cls):
        if cls.__app_driver is None:
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '5.1'
            desired_caps['deviceName'] = '192.168.10.10:9999'
            desired_caps['appPackage'] = page.appPackage
            desired_caps['appActivity'] = page.appActivity
            cls.__app_driver = appium.webdriver.Remote("http://127.0.0.1:4444/wd/hub", desired_caps)
        return cls.__app_driver

    @classmethod
    def quit_app_driver(cls):
        if cls.__app_driver is not None:
            cls.__app_driver.quit()
            cls.__app_driver = None
